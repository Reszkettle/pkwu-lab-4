

from enum import Enum
from typing import Optional
from dataclasses import dataclass


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
