================================================================
  AI기반 타겟고객 Buying Center 분석기
  (Target Customer Buying Center Analyzer)
  나눔경영컨설팅
================================================================

[프로젝트 개요]
회사명과 제품/상품을 입력하면 AI(Claude)가 타겟 고객을 자동 분석하는
웹앱입니다. B2C, B2B, B2G 각 유형별로 고객 역할을 분류하고,
역할별 페르소나, Pain Point, 가치제안(Value Proposition)을 생성합니다.

[Buying Center 개념]
Buying Center(구매센터)는 B2B 마케팅에서 구매 의사결정에 관여하는
역할자 그룹을 의미합니다. 각 역할자의 니즈와 관점을 이해하면
효과적인 영업/마케팅 전략을 수립할 수 있습니다.

[주요 기능]
- B2C 고객 역할 분석: 사용자 / 구매결정자 / 영향력자 (3가지)
- B2B 구매센터 분석: Decider / Buyer / Influencer / Initiator / User / Gatekeeper (6가지)
- B2G 공공부문 분석: 타겟 기관, 조달 프로세스, 의사결정 기준
- 고객사 산업(Industry) 및 어플리케이션(Application) 분류
- 역할별 페르소나, Pain Point, 가치제안 자동 생성
- 결과 저장: PDF / HTML 다운로드 / 텍스트 복사
- 분석 진행 상태 표시 (5단계 프로그레스 바)
- API 키 로컬 저장 (localStorage)
- 반응형 디자인 (모바일 대응)
- 인쇄 최적화 (CSS @media print)

[파일 구성]
- Buying-center_analyzer.html : 메인 웹앱 (프론트엔드, 브라우저에서 직접 API 호출)
- app.py                      : Flask 백엔드 버전 (서버 경유 API 호출, 참고용)
- readme.txt                  : 프로젝트 설명 (이 파일)
- .gitignore                  : Git 추적 제외 설정

※ HTML 파일만으로 완전히 독립 동작합니다. app.py는 서버 방식의 참고 코드입니다.

[사용 방법]
1. 웹앱을 열고 Anthropic API 키를 입력
2. 회사/조직명 입력 (예: 경동나비엔, 현대코퍼레이션)
3. 취급 제품/상품 입력 (예: 보일러, 변압기)
4. "분석 시작" 버튼 클릭
5. AI가 B2C/B2B/B2G 타겟 고객을 자동 분석
6. 결과를 PDF/HTML/텍스트로 저장 가능

[기술 스택]
- 프론트엔드: HTML5, CSS3, Vanilla JavaScript (단일 파일)
- AI: Anthropic Claude Haiku 4.5 API (브라우저 직접 호출)
- 폰트: Pretendard (Google Fonts CDN)
- 백엔드: 없음 (GitHub Pages 배포용)
- 참고: app.py는 Flask + anthropic 패키지 사용 (서버 방식)

[개발 환경 및 배포]
- 소스 코드: Google Drive (01.나눔경영컨설팅 웹앱(코딩)★/002.Buying-center_analyzer/)
- Git 저장소: Google Drive 폴더에서 직접 Git 관리
- GitHub: jazzmania74/Buying-center-analyzer (main 브랜치)
- 배포 URL: https://jazzmania74.github.io/Buying-center-analyzer/Buying-center_analyzer.html
- 수정 후 배포: git add → git commit → git push origin main → GitHub Pages 자동 반영

[주의사항]
- Anthropic API 키가 필요합니다 (사용자가 직접 입력)
- API 키는 브라우저의 localStorage에만 저장되며 서버로 전송되지 않습니다
- API 호출 비용은 Anthropic 계정에 청구됩니다

================================================================
