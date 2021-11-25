from fastapi import FastAPI


app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string(request: InAnalyseString):
    output_str = process_request(request)
    return output_str


@app.post(path="/format-analysed-string")
async def format_analysed_string(request: InFormatAnalysedString):
    output_str = format_analysis(request)
    return output_str
