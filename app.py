import os
import json
from flask import Flask, request, jsonify, send_from_directory
import anthropic

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    company_name = data.get("company_name", "").strip()
    products = data.get("products", "").strip()

    api_key = data.get("api_key", "").strip()

    if not company_name or not products:
        return jsonify({"error": "회사명과 제품/상품을 모두 입력해주세요."}), 400

    if not api_key:
        return jsonify({"error": "API 키를 입력해주세요."}), 400

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""당신은 마케팅 전략 전문가이자 고객 분석 전문가입니다.

아래의 회사/조직과 취급하는 제품/상품 정보를 분석하여 다음을 수행해주세요.

## 입력 정보
- 회사/조직명: {company_name}
- 취급 제품/상품: {products}

## 분석 요청

1. **타겟 고객 유형 판별**: B2C, B2B, B2G 중 어디에 해당하는지 판별하세요. 복수 선택 가능합니다.

2. **고객사의 산업 및 어플리케이션 분류**: 이 제품/상품을 구매하는 고객사(타겟 고객)가 속한 산업(Industry)과 어플리케이션(Application) 영역을 분석하세요. 즉, 판매하는 회사가 아니라 구매하는 고객이 어떤 산업에서 어떤 용도로 사용하는지를 기준으로 분석합니다.

3. **고객 역할별 분석**:

### B2C인 경우:
다음 세 가지 역할별로 분석하세요:
- **사용자(User)**: 실제 제품을 사용하는 사람
- **구매결정자(Decision Maker)**: 구매를 최종 결정하는 사람
- **영향력자(Influencer)**: 구매 결정에 영향을 미치는 사람

각 역할별로 다음을 제공하세요:
- 페르소나 (나이, 성별, 직업, 특성 등)
- 핵심 니즈/Pain Point
- 가치제안 (Value Proposition)

### B2B인 경우:
다음 여섯 가지 역할별로 분석하세요:
- **Decider (최종결정자)**: 최종 구매 결정 권한을 가진 사람
- **Buyer (구매담당자)**: 실제 구매 프로세스를 진행하는 사람
- **Influencer (영향력자)**: 기술적/전문적 의견을 제시하는 사람
- **Initiator (발의자)**: 구매 필요성을 처음 제기하는 사람
- **User (사용자)**: 실제 제품/서비스를 사용하는 사람
- **Gatekeeper (정보통제자)**: 정보 흐름을 통제하는 사람

각 역할별로 다음을 제공하세요:
- 부서 (Department)
- 페르소나 (직책, 특성)
- Pain Point
- 가치제안 (Value Proposition)

### B2G인 경우:
정부/공공기관 대상 판매의 특성을 분석하고:
- 주요 타겟 기관/부서
- 조달 프로세스 특성
- 핵심 의사결정 기준
- 가치제안 (Value Proposition)

반드시 아래 JSON 형식으로 응답하세요. JSON만 출력하고 다른 텍스트는 포함하지 마세요.

```json
{{
  "company_name": "회사명",
  "products": "제품/상품",
  "target_types": ["B2C", "B2B", "B2G"],
  "industry": {{
    "name": "고객사의 산업명",
    "application": "고객사의 어플리케이션 영역",
    "description": "고객사가 이 제품을 사용하는 산업 및 어플리케이션에 대한 간략 설명"
  }},
  "b2c": {{
    "applicable": true/false,
    "roles": [
      {{
        "role": "사용자(User)",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "구매결정자(Decision Maker)",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "영향력자(Influencer)",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }}
    ]
  }},
  "b2b": {{
    "applicable": true/false,
    "roles": [
      {{
        "role": "Decider (최종결정자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "Buyer (구매담당자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "Influencer (영향력자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "Initiator (발의자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "User (사용자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }},
      {{
        "role": "Gatekeeper (정보통제자)",
        "department": "부서명",
        "persona": "페르소나 설명",
        "pain_points": ["Pain Point 1", "Pain Point 2"],
        "value_proposition": "가치제안"
      }}
    ]
  }},
  "b2g": {{
    "applicable": true/false,
    "target_agencies": ["기관/부서 1", "기관/부서 2"],
    "procurement_characteristics": "조달 프로세스 특성",
    "decision_criteria": ["기준 1", "기준 2"],
    "value_proposition": "가치제안"
  }}
}}
```

applicable이 false인 섹션은 빈 데이터로 두되 구조는 유지하세요.
분석은 한국어로 작성하세요."""

    try:
        with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=8192,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()

        response_text = ""
        for block in response.content:
            if block.type == "text":
                response_text += block.text

        # Extract JSON from response
        json_text = response_text.strip()
        if json_text.startswith("```json"):
            json_text = json_text[7:]
        if json_text.startswith("```"):
            json_text = json_text[3:]
        if json_text.endswith("```"):
            json_text = json_text[:-3]
        json_text = json_text.strip()

        result = json.loads(json_text)
        return jsonify(result)

    except json.JSONDecodeError as e:
        return jsonify({
            "error": f"AI 응답 파싱 오류: {str(e)}",
            "raw_response": response_text,
        }), 500
    except anthropic.APIError as e:
        return jsonify({"error": f"API 오류: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"서버 오류: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
