# pkwu-lab-4

# Routes

You'll find here the routes exposed by this repository. Note that you can also review them through the interactive API docs. The interactive API docs are located at `/docs` and `/redoc`

## String router

<br>

### **Analyse string**

#### POST `/analyse-string`

#### **Description**:

Uses an external api for analyzing the string and formatting the output into given format.
Link to the external api documentation: [formatted analyse string docs](https://github.com/Reszkettle/pkwu-lab-3#readme)

#### **Request Body**

| Type     | Name                  | Optional | Description                                                     |
| -------- | --------------------- | -------- | --------------------------------------------------------------- |
| `string` | string                | No       | string that will be analyzed                                    |
| `string` | substring             | Yes      | optional substring which occurrences will be counted            |
| `string` | firstConversionFormat | No       | first conversion format of analysis ( json / xml / csv / text ) |
| `string` | outputFormat          | No       | ouput format ( json / xml / csv / text )                        |

### Response

On success (HTTP 200 status) this endpoint returns single string that contains the structure for the format that you've provided in request body:

Example for Request Body:

```json
{
	"string": "Nieborak1#",
	"substring": "rak",
	"firstConversionFormat": "csv",
	"outputFormat": "..."
}
```

### Response string when `outputFormat` is:

- json
  ```json
  {
  	"lower_case_letters_count": 7,
  	"upper_case_letters_count": 1,
  	"digits_count": 1,
  	"special_characters_count": 1,
  	"substring_occurrences_count": 1
  }
  ```
- xml
  ```xml
  <?xml version=\"1.0\" encoding=\"UTF-8\" ?>
  <string-analyze-statistics>
    <lower_case_letters_count>7</lower_case_letters_count>
    <upper_case_letters_count>1</upper_case_letters_count>
    <digits_count>1</digits_count>
    <special_characters_count>1</special_characters_count>
    <substring_occurrences_count>1</substring_occurrences_count>
  </string-analyze-statistics>
  ```
- csv
  ```csv
  lower_case_letters_count,upper_case_letters_count,digits_count,special_characters_count,substring_occurrences_count
  7,1,1,1,1
  ```
- text
  ```
  lower_case_letters_count: 7, upper_case_letters_count: 1, digits_count: 1, special_characters_count: 1, substring_occurrences_count: 1
  ```

<br>

### **Format Analysed String Output**:

#### POST `/format-analysed-string`

#### **Description**:

Formats the string analysis to the given format.

#### **Request Body**

| Type     | Name         | Optional | Description                                            |
| -------- | ------------ | -------- | ------------------------------------------------------ |
| `string` | inputFormat  | No       | input format of analysis ( json / xml / csv / text )   |
| `string` | analysis     | No       | analysis result that will be formatted to given format |
| `string` | outputFormat | No       | ouput format ( json / xml / csv / text )               |

### Response

On success (HTTP 200 status) this endpoint returns single string that contains the analysis in the format that you've provided in request body:
Example for Request Body:

```json
{
	"inputFormat": "xml",
	"outputFormat": "json",
	"analysis": "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
                <string-analyze-statistics>
                    <lower_case_letters_count>7</lower_case_letters_count>
                    <upper_case_letters_count>1</upper_case_letters_count>
                    <digits_count>1</digits_count>
                    <special_characters_count>1</special_characters_count>
                    <substring_occurrences_count>1</substring_occurrences_count>
                </string-analyze-statistics>"
}
```

### Response string when `outputFormat` is:

- json

  ```json
  {
  	"lower_case_letters_count": 7,
  	"upper_case_letters_count": 1,
  	"digits_count": 1,
  	"special_characters_count": 1,
  	"substring_occurrences_count": 1
  }
  ```

- xml
  ```xml
  <?xml version=\"1.0\" encoding=\"UTF-8\" ?>
  <string-analyze-statistics>
    <lower_case_letters_count>7</lower_case_letters_count>
    <upper_case_letters_count>1</upper_case_letters_count>
    <digits_count>1</digits_count>
    <special_characters_count>1</special_characters_count>
    <substring_occurrences_count>1</substring_occurrences_count>
  </string-analyze-statistics>
  ```
- csv
  ```csv
  lower_case_letters_count,upper_case_letters_count,digits_count,special_characters_count,substring_occurrences_count
  7,1,1,1,1
  ```
- text
  ```
  lower_case_letters_count: 7, upper_case_letters_count: 1, digits_count: 1, special_characters_count: 1, substring_occurrences_count: 1
  ```
