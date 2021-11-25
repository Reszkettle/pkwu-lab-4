from typing import Optional
from fastapi import FastAPI
from dataclasses import dataclass
from enum import Enum


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


def process_request(request: InAnalyseString):
    pass


def format_analysis(request: InFormatAnalysedString):
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
