from typing import Optional
from fastapi import FastAPI
from dataclasses import dataclass
from enum import Enum
import requests as req


class AnalysisFormat(str, Enum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    TEXT = "text"


@dataclass
class InAnalyseString:
    firstConversionFormat: AnalysisFormat
    outputFormat: AnalysisFormat
    string: str
    substring: Optional[str]


@dataclass
class InFormatAnalysedString:
    inputFormat: AnalysisFormat
    outputFormat: AnalysisFormat
    analysis: str


EXTERNAL_ENDPOINT = 'http://127.0.0.1:8002/analyse-string'


def process_request(request: InAnalyseString):
    response = req.post(EXTERNAL_ENDPOINT, json={
        "string": request.string, "substring": request.substring, "format": request.firstConversionFormat})
    if response.status_code == 200:
        analysis_string = response.json()
        format_analysis(analysis_string,
                        request.firstConversionFormat, request.outputFormat)


def format_analysis(analysis_string: str, input_format: str, output_format: str):
    pass


app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string(request: InAnalyseString):
    output_str = process_request(request)
    return output_str


@app.post(path="/format-analysed-string")
async def format_analysed_string(request: InFormatAnalysedString):
    output_str = format_analysis(request)
    return output_str
