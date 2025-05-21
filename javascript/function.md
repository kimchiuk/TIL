### 화살표함수와 함수 선언식 비교


함수 선언식
```javascript
const sum = (a, b) => {
    return a + b;
}
```

화살표 함수
```javascript
function sum(a, b) {
    a + b;
}
```


---

this 바인딩

- 일반함수
```javascript
const obj = {
  value: 10,
  getValue: function () {
    return this.value;
  }
};

console.log(obj.getValue()); // 10
```
`동적`으로 바인딩됨 (호출 위치 기준)


- 화살표 함수
```javascript
const obj = {
  value: 10,
  getValue: () => {
    return this.value;
  }
};

console.log(obj.getValue()); // undefined (또는 window.value)
```
`정적`으로 바인딩됨 (선언된 위치의 this를 캡쳐)

화살표 함수는 자신만의 this를 가지지 않고, 외부 스코프의 this를 그대로 사용함


---
`arguments` 객체 사용가능 여부


- 일반 함수
```javascript
function test() {
  console.log(arguments);
}
test(1, 2, 3); // [1, 2, 3]
```


- 화살표 함수
```js
const test = () => {
  console.log(arguments);
};  

arrowTest(1, 2, 3); //  ReferenceError: arguments is not defined에러

```
화살표 함수에서는 `...args`로 대체

```js
const test = (...args) => {
  console.log(args);
};

test(1, 2, 3);
// 출력: [1, 2, 3]
```

---
생성자 함수 사용가능 여부

- 일반 함수
```js
function Person(name) {
  this.name = name;
}
const p1 = new Person("Kim"); // OK
```


- 화살표 함수
```js
const Person = (name) => {
  this.name = name;
};
const p1 = new Person("Kim"); // TypeError: PersonArrow is not a constructor
```

| 항목             | 일반 함수 | 화살표 함수  |
| -------------- | ----- | ------- |
| `new`로 인스턴스 생성 | ✅ 가능  | ❌ 에러 발생 |



--- 
호이스팅

- 일반 함수 선언식은 완전히 호이스팅됨

```js
sayHello(); // "안녕!"

function sayHello() {
  console.log("안녕!");
}

```

- 화살표 함수는 변수 호이스팅만 되고 초기화는 안 됨

```js
sayHello(); // TypeError: sayHello is not a function

const sayHello = () => {
  console.log("안녕!");
};

```

const sayHello는 변수 자체는 호이스팅되지만,
초기화 전에 접근하려 하면 에러 발생 (일명 TDZ: Temporal Dead Zone 때문)

--- 
TDZ란?

`let`, `const`, `class`로 선언된 변수가 실제 선언되기 전까지 접근할 수 없는 구간을 의미함.

```js
// 변수 선언 전에 접근하면 ReferenceError 발생

console.log(myName); // ReferenceError: Cannot access 'myName' before initialization
let myName = "kim";
```

TDZ는 왜 생기는가?

- var는 선언과 동시에 undefined로 초기화되기 때문에 TDZ가 없음

- let, const, class는 초기화되기 전까지는 아예 접근 불가하도록 설계됨

- 코드의 예측 가능성과 오류 방지를 위해서

- 함수 선언문은 TDZ 없음. (완전히 호이스팅 됨)

```js
console.log(sayHi()); // "Hi"

function sayHi() {
  return "Hi";
}
```

TDZ를 피하는 팁

1. 변수 선언은 항상 위쪽에서 먼저 하자

2. let, const, class는 선언 전에 절대 접근하지 말자

3. 화살표 함수도 선언 이후에만 호출하자