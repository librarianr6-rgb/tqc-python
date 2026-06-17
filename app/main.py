from __future__ import annotations
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse,HTMLResponse, JSONResponse
from pathlib import Path

import os
import re
import importlib
from typing import Any, Dict, List
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="TQC+ Python 題庫（動態版）")
# ✅ 你的題目 API 檔案位置：app/tqc/q106.py
TQC_DIR = Path(__file__).resolve().parent / "tqc"

# 靜態檔案（如果你沒有 static 也沒關係，把這行註解掉即可）
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

_Q_RE = re.compile(r"^q(\d+)\.py$", re.IGNORECASE)


def load_questions() -> List[Dict[str, Any]]:
    """掃描 app/tqc 找到 qxxx.py，讀取 TITLE / INPUTS / OUTPUT_HINT。"""
    folder = os.path.join("app", "tqc")
    questions: List[Dict[str, Any]] = []

    for fname in os.listdir(folder):
        m = _Q_RE.match(fname)
        if not m:
            continue

        qid = m.group(1)
        module = importlib.import_module(f"app.tqc.{fname[:-3]}")  # app.tqc.q104

        questions.append(
            {
                "id": qid,
                "title": getattr(module, "TITLE", f"TQC {qid}"),
                "inputs": list(getattr(module, "INPUTS", [])),
                "output_hint": getattr(module, "OUTPUT_HINT", ""),
            }
        )

    questions.sort(key=lambda x: int(x["id"]))
    return questions


def get_module(qid: str):
    """qid=104 -> app.tqc.q104"""
    if not re.fullmatch(r"\d+", qid):
        raise ValueError("題號格式錯誤")
    return importlib.import_module(f"app.tqc.q{qid}")


# -------------------------
# Pages
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # 關鍵錯誤
    # return templates.TemplateResponse("index.html", {"request": request, "title": "題庫首頁"})
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"title": "題庫首頁"}
)


@app.get("/tqc/{qid}", response_class=HTMLResponse)
def tqc_single(request: Request, qid: str):
    try:
        module = get_module(qid)
        qtitle = getattr(module, "TITLE", f"TQC {qid}")
        inputs = getattr(module, "INPUTS", [])
    except Exception:
        qtitle = "題目不存在"
        inputs = []

    return templates.TemplateResponse(
        "tqc_single.html",
        {
            "request": request,
            "title": f"TQC {qid}",
            "qid": qid,
            "qtitle": qtitle,
            "inputs": inputs,
        },
    )


# -------------------------
# APIs
# -------------------------
@app.get("/api/questions", response_class=JSONResponse)
def api_questions():
    return load_questions()


@app.post("/api/tqc/{qid}", response_class=JSONResponse)
async def api_run_tqc(qid: str, request: Request):
    try:
        module = get_module(qid)
    except Exception:
        return {"ok": False, "error": "題目不存在"}

    try:
        data = await request.json()
        if not isinstance(data, dict):
            return {"ok": False, "error": "Body 必須是 JSON object"}
    except Exception:
        return {"ok": False, "error": "Body 解析失敗（請用 JSON）"}

    try:
        out = module.solve(data)
        if not isinstance(out, dict):
            return {"ok": False, "error": "solve() 必須回傳 dict"}
        return {"ok": True, "qid": qid, **out}
    except Exception as e:
        return {"ok": False, "error": f"執行錯誤：{e}"}


@app.get("/healthz", response_class=JSONResponse)
def healthz():
    return {"ok": True}

@app.get("/api/question/{qid}", response_class=JSONResponse)
def api_question(qid: str):
    try:
        module = get_module(qid)
    except Exception:
        return {"ok": False, "error": "題目不存在"}

    return {
        "ok": True,
        "id": qid,
        "title": getattr(module, "TITLE", f"TQC {qid}"),
        "inputs": list(getattr(module, "INPUTS", [])),
        "input_meta": getattr(module, "INPUT_META", {}),
        "output_hint": getattr(module, "OUTPUT_HINT", ""),
    }

@app.get("/api/source/{qid}", response_class=PlainTextResponse)
def get_source(qid: str):
    """
    回傳指定題號的 API 程式碼內容，例如 /api/source/106 -> q106.py
    """
    # ✅ 只允許 3~4 位數字（你若只用 3 位就改成 r"^\d{3}$"）
    if not re.fullmatch(r"\d{3,4}", qid):
        raise HTTPException(status_code=400, detail="Invalid qid")

    filename = f"q{qid}.py"
    path = (TQC_DIR / filename).resolve()

    # ✅ 防止路徑穿越：確保檔案仍在 TQC_DIR 底下
    if TQC_DIR.resolve() not in path.parents:
        raise HTTPException(status_code=400, detail="Invalid path")

    if not path.exists():
        raise HTTPException(status_code=404, detail=f"{filename} not found")

    try:
        code = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        code = path.read_text(encoding="utf-8", errors="replace")

    return code

@app.get("/api/answer/{qid}", response_class=PlainTextResponse)
def get_answer_source(qid: str):
    """
    回傳指定題號的題庫解答內容
    例如：
    /api/answer/101 -> PYA101.py
    """
    if not re.fullmatch(r"\d{3,4}", qid):
        raise HTTPException(status_code=400, detail="Invalid qid")


    filename = f"PYA{qid}.py"
    path = (TQC_DIR / filename).resolve()


    # 防止路徑穿越
    if TQC_DIR.resolve() not in path.parents:
        raise HTTPException(status_code=400, detail="Invalid path")


    if not path.exists():
        raise HTTPException(status_code=404, detail=f"{filename} not found")


    try:
        code = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        code = path.read_text(encoding="utf-8", errors="replace")


    return code