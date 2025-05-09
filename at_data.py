# -*- coding: utf-8 -*-
"""AT_DATA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DZwlBVIirUMWEmJrpTGJGRAUrFQqFENu
"""

import random
import string

# 계급 목록 (하사 이상)
ranks = ['하사', '중사', '상사', '원사', '소위', '중위', '대위']

# 성과 이름 요소
last_names = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임','송','엄']
first_names = ['맹수', '동훈', '준서', '지우', '동현', '짜오', '경웅', '유진', '현우', '수빈', '예린', '지민', '준호', '채원']

# A ~ Z 부대 리스트 생성
units = [f"{chr(65+i)}부대" for i in range(26)]  # A~Z 부대

# 군인 생성 함수
def generate_soldier(unit):
    rank = random.choice(ranks)
    name = random.choice(last_names) + random.choice(first_names)
    personal_number = f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    unit_number = f"{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    return {
        "계급": rank,
        "이름": name,
        "소속": unit,
        "개인번호": personal_number,
        "군부대번호": unit_number
    }

# 26명 생성 (A~Z부대 각각 1명씩)
soldiers = [generate_soldier(unit) for unit in units]

# 출력
for s in soldiers:
    print(f"{s['계급']} {s['이름']} | 소속: {s['소속']} | 개인번호: {s['개인번호']} | 군부대번호: {s['군부대번호']}")

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>네트워크 당직사령 전화번호부</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        input[type="text"] {{
            margin-bottom: 10px;
            padding: 5px;
            width: 300px;
            font-size: 14px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #aaa;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        td[contenteditable="true"] {{
            background-color: #fdfde3;
        }}
    </style>
    <script>
        function filterTable() {{
            var input = document.getElementById("searchInput");
            var filter = input.value.toUpperCase();
            var table = document.getElementById("soldierTable");
            var tr = table.getElementsByTagName("tr");

            for (var i = 1; i < tr.length; i++) {{
                var tds = tr[i].getElementsByTagName("td");
                var show = false;
                for (var j = 0; j < tds.length; j++) {{
                    if (tds[j]) {{
                        var txt = tds[j].textContent || tds[j].innerText;
                        if (txt.toUpperCase().indexOf(filter) > -1) {{
                            show = true;
                            break;
                        }}
                    }}
                }}
                tr[i].style.display = show ? "" : "none";
            }}
        }}
    </script>
</head>
<body>
    <h1>군인 명단</h1>
    <input type="text" id="searchInput" onkeyup="filterTable()" placeholder="검색어를 입력하세요 (이름, 소속 등)">
    <table id="soldierTable">
        <thead>
            <tr>
                <th>번호</th>
                <th>계급</th>
                <th>이름</th>
                <th>소속</th>
                <th>개인번호</th>
                <th>군부대번호</th>
            </tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
</body>
</html>
"""

def generate_table_rows(soldiers):
    rows = ""
    for i, s in enumerate(soldiers, start=1):
        rows += (
            f"<tr>"
            f"<td>{i}</td>"
            f"<td contenteditable='true'>{s['계급']}</td>"
            f"<td>{s['이름']}</td>"
            f"<td>{s['소속']}</td>"
            f"<td contenteditable='true'>{s['개인번호']}</td>"
            f"<td contenteditable='true'>{s['군부대번호']}</td>"
            f"</tr>\n"
        )
    return rows

rows_html = generate_table_rows(soldiers)
full_html = html_template.format(table_rows=rows_html)

# HTML 파일로 저장
with open("soldiers_NUMBER.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("✅ soldiers_NUMBER.html 파일이 생성되었습니다.")