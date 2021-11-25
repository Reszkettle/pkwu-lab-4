from typing import Optional
from fastapi import FastAPI
from dataclasses import dataclass
from enum import Enum
import requests as req
import csv
import json
import io


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
    substring: Optional[str] = None


@dataclass
class InFormatAnalysedString:
    input_format: AnalysisFormat
    output_format: AnalysisFormat
    analysis: str


EXTERNAL_ENDPOINT = 'http://127.0.0.1:8002/analyse-string'


def process_request(request: InAnalyseString):
    print(request.firstConversionFormat)
    print(request.outputFormat)
    response = req.post(EXTERNAL_ENDPOINT, json={
        "string": request.string, "substring": request.substring, "format": request.firstConversionFormat})
    if response.status_code == 200:
        analysis_string = response.text
        print(analysis_string)
        return format_analysis(InFormatAnalysedString(
            input_format=request.firstConversionFormat,
            output_format=request.outputFormat,
            analysis=analysis_string))


def format_analysis(request: InFormatAnalysedString):

    if request.input_format == request.output_format:
        return request.analysis

    json_dict = format_to_json(request.analysis, request.input_format)

    if request.output_format == AnalysisFormat.CSV:
        pass
    elif request.output_format == AnalysisFormat.JSON:
        pass
    elif request.output_format == AnalysisFormat.TEXT:
        pass
    else:
        pass


def format_to_json(analysis_string: str, format: AnalysisFormat) -> dict:

    if format == AnalysisFormat.JSON:
        return json.loads(analysis_string)

    elif format == AnalysisFormat.CSV:
        [str_keys, val_keys] = analysis_string.strip('"').split('\\n')
        keys = str_keys.split(',')
        values = [int(v) for v in val_keys.split(',') if v != 'None']
        return dict(zip(keys, values))
    elif format == AnalysisFormat.XML:
        pass
    else:
        d = dict()
        for key_val in analysis_string.strip('"').split(', '):
            [key, val] = key_val.split(': ')
            if val != 'None':
                d[key] = int(val)


app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string(request: InAnalyseString):
    output_str = process_request(request)
    return output_str


@app.post(path="/format-analysed-string")
async def format_analysed_string(request: InFormatAnalysedString):
    output_str = format_analysis(request)
    return output_str
