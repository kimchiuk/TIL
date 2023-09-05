# 웹

World Wide Web

- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

web

- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

web site

- 인터넷에서 여러 개의 web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

web page

- HTML, CSS 등의 웹 기술을 이용하여 만들어진, "Web site"를 구성하는 하나의 요소

# HTML

웹 페이지의 의미와 구조를 정의하는 언어

hypertext
- 웹페이지를 다른페이지로 연결하는 링크
- 참조를 통해 사용자가한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

markup language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- ex) HTML, Markdown

## HTML 구조

- \<!DOCTYPE html>
  - 해당 문서가 html로 문서라는 것을 나타냄
- \<html>\</html>
  - 전체 페이지의 콘텐츠를 포함
- \<title>\</title>
  - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- \<head>\</head>
  - HTML 문서에 관련된 설명, 설정 등
  - 사용자에게 보이지 않음
- \<body>\</body>
  - 페이지에 표시되는 모든 콘텐츠

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My page</title>
</head>
<body>
  <p>This is my page</p>
</body>
</html>

```

### HTML 요소

하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
닫는 태그는 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

### HTML 속성

규칙
- 속성은 요소 이름과 속성 사이에 공백이 있어야 함
- 하나 이상의 속성들이 있는 경우엔 속서 사이에 공백으로 구분함
- 속성 값은 열고 닫는 따옴표로 감싸야 함

목적
- 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
- css에서 해당 요소를 선택하기 위한 값으로 활용됨

## text structure

html text structure 
- html의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

\<h1?>Heading\</h1>
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재문서의 최상위 제목이라는 의미를 부여하는 것 (시맨틱 태그)

대표적인 HTML text structure
- heading (제목) & Paragraphs (문단)
  - h1~6, p

- Lists
  - ol (숫자), ul (숫자 없는), li

- Emphasis & Importance (강조)
  - em, strong 

```
<body>
  <h1>main heading</h1>
  <h2>sub heading</h2>
  <p>this is my page</p>
  <p>this is <em>emphasis</em></p>
  <p>Hi my <strong>name is</strong> air</p>
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ol>
</body>
```

# 웹 스타일링 CSS 

웹 페이지의 디자인과 레이아웃을 구성하는 언어

## CSS 적용 방법

1. 인라인 스타일
  - html 요소 안에 style 속성 값으로 작성
2. 내부 스타일 시트
  - head 태그 안에 style 태그에 작성
3. 외부 스타일 시트
  - 별도의 css 파일 생성 후 html link 태그를 사용해 불러오기

## css 선택자

css 선택자 특징

- 전체 선택자 (*)
  - html 모든 요소를 선택
- 요소 선택자
  - 지정한 모든 태그를 선택
- 클래스 선택자 ('.' (dot))
  - 주어진 클래스 속성을 가진 모든 요소를 선택
- 아이디 선택자 ('#')
  - 주어진 아이디 속성을 가진 요소 선택
  - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
- 자손 결합자 (" " (space))
  - 첫 번째 요소의 자손 요소들 선택
  - 예) p span은 \<p> 안에 있는 모든 \<span>를 선택 (하위 레벨 상관 없이)
- 자식 결합자 (">")
  - 첫 번째 요소의 직계 자식만 선택
  - 예) ul > li은 \<ul> 안에 있는 모든 \<li>를 선택 (한단계 아래 자식들만)

## 우선순위

동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 적용되는지 결정하는 것

cascade 계단식
- 동일한 우선순위를 같은 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용됨

우선순위가 높은 순

1. importance
  - !important
2. inline 스타일
3. 선택자
  - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 순서

!important
다른 우선순위 규칙보다 원하여 적용하는 키워드

cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음

## 상속

css 상속
- 기본적으로 css는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

상속 여부
- 상속 되는 속성
  - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
  - Box model 관련 요소 (width, height, border, box-sizing...)
    position 관련 요소 (position, top/right/bottom/left, z-index) 등

css 상속 여부는 MDN 문서에서 확인하기
- MDN 각 속성별 문서 하단에서 상속 여부를 확인할 수 있음

# 참고

HTML 관련 사항
- 요소(태그) 이름은 대소문자를 구분하지 않지만 "소문자" 사용을 권장
- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 "큰 따옴표" 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성시 주의

CSS 인라인 스타일은 사용하지 말 것
- CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦

CSS의 모든 속성을 외우는 것이 아님
- 자주 사용되는 속성은 그리 많지 않으며 주로 활용 하는 속성 위주로 사용하다 보면 자연스럽게 익히게 됨
- 그 외 속성들은 개발하며 필요할 때마다 검색해서 학습 후 사용할 것

속성은 되도록 'class'만 사용할 것
- id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
- 문서에서 단 한번 유일하게 적용될 스타일에 경우에만 id 선택자 사용을 고려
