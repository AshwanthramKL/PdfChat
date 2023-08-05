# PdfChat with llama2

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Demo](#demo)
  - [Sample Query](#sample-query)
  - [Sample Output](#sample-output)

## Description

PdfChat is a application where you can chat with your research paper in pdf format. You can ask questions to your pdf and it will answer you. It is a fun way to interact with your pdf.

## Installation

1. Clone the repository
2. Install the requirements using the following command

```bash
pip install -r requirements.txt
```

3. Add your pdf files to the `data/` folder or you can use the sample pdf files provided in the folder.

4. Ensure you have downloaded the 8-bit quantised GGML binary file from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main and placed it into the `models/` folder

![](assets/llama_model.jpeg)

5. To start parsing user queries into the application, launch the terminal from the project directory and run the following command:

```bash
python main.py "<user query>"
```

```
Note:
The user query should be in double quotes.
It takes the application about 2-3 minutes to load the model, parse the query and provide an answer.
```

---

## Demo

### Sample Query

`Tell me about Query2doc?`

![Sample Query](assets/cmd_line_query.png)

### Sample Output

![Sample Output](assets/cmd_line_response.png)
