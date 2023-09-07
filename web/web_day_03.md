# bootstrap

css 프론트엔드 프레임워크 (toolkit)
- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

bootstrap 기본 사용법
```
<p class="mt-5">Hello, world!</p>
```
mt-5
{property}{sides}{size}

bootstrap에서 클래스 이름으로 spacing을 표현하는 방법

property
- m : margin
- p : padding

sides
- t : top
- b : bottom
- s : left
- e : right
- y : top, bottom
- x : left, right
- blank : 4 sides

size
- 0 : 0rem : 0px
- 1 : 0.25rem : 4px
- 2 : 0.5rem : 8px
- 3 : 1 rem : 16px
- 4 : 1.5rem : 24px
- 5 : 3rem : 48px
- auto : auto : auto

bootstrap에는 특정한 규칙이 있는 클래스 이름으로 이미 스타일 및 레이아웃으로 작성되어 있음

## typography
제목, 본문텍스트, 목록

## color
text, border, background 및 다양한 요소에 사용하는 bootstrap의 색상 키워드

## component
bootstrap에서 제공하는 UI 관련 요소
-> 버튼, 네비게이션 바, 카드, 폴, 트롤다운 ...

컴포넌트의 이점
- 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용

# Semantic web
웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

이 요소가 시작적으로 어떻게 보여질까? -> 이 요소가 가진 목적과 역할은 무엇일까?

단순히 최상위 제목"처럼" 보이게 출력하는 것 vs 페이지 최 상위 제목 의미를 제공하는 semantic 요소 h1, 브라우저의 의해 제목처럼 보이도록 스타일이 지정됨

HTML Semantic Element
- 기본적인 모양과 기능 이외에 의미를 가지는 HTML요소
- 검색 엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록

## semantic in css

OOCSS (object oriented css)
- 객체 지향적 접근법을 적용하여 css를 구성하는 방법론

css 방법론
- css를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

oocss 기본원칙
1. 구조와 스킨을 분리
2. 컨테나와 콘텐츠를 분리

구조와 스킨 분리
- 구조와 스킨을 분리함으로써 재사용 가능성을 높임
- 모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의

컨테이너와 콘텐츠 분리
- 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
- 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함
- 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

OOCSS 기본 원칙
- .header와 footer 클래스가 폰트 크기와 색 둘 다 영향을 줌.
  - .container .title 이 폰트 크기 담당 (콘텐츠 스타일)
  - .header와 .footer가 폰트 색 담당(컨테이너 스타일)

```
/* bad */
.header h2{
font-size: 24px;
color: white;
}

.footer h2 {
font-size: 24px;
color: black;
}
```

```
/* good */
.container .title {
font-size: 24px;
}

.header {
color: white;
}

. footer {
color: black;
}
```
