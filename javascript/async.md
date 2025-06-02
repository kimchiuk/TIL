### 동기, 비동기

- 비동기 작업이란 특정 코드의 로직이 끝날 때까지 기다리지 않고, 나머지 코드를 먼저 실행하는 것.
- 빠른 페이지 로딩을 위해 웹개발에서 비동기를 사용함.

동기

- 코드가 위에서 아래로 한 줄씩 실행됨
- 하나 끝나야 다음 줄 실행됨

```js
console.log("1");
console.log("2");
console.log("3");

// 출력: 1, 2, 3
```

---

비동기

- 작업을 백그라운드에 넘기고 다음 줄을 먼저 실행함
- `setTimeout`, `setInterval`
- `fetch`, `axios` 등 API 요청
- 이벤트 핸들러(`addEventListener`)
- 파일 I/O (Node.js)

```js
console.log("1");

setTimeout(() => {
  console.log("2");
}, 1000);

console.log("3");

// 출력: 1, 3, 2
```

`setTimeout`이 비동기로 동작해서 1, 3, (1초뒤) 2 순으로 실행됨

---

콜백 함수

- 비동기 작업이 끝난 후 호출될 함수를 전달하는 방식

```js
fucntion fetchData(callback) {
    setTimeout(() => {
        const data = {name: 'kim'};
        callback(data);
    }, 1000);
}

fetchData((result) => {
    console.log(result);  // 1초 후 {name: 'kim'}
})

```

---

콜백 지옥

```js
getUser(id, (user) => {
  getPosts(user.id, (posts) => {
    getComments(posts[0], (comments) => {
      console.log(comments);
    });
  });
});
```

개선 코드

```js
async function process() {
  try {
    const user = await getUser(1);
    const posts = await getPosts(user.id);
    const comments = await getComments(posts[0]);
    console.log(comments);
  } catch (err) {
    console.error("에러 발생:", err);
  }
}

process();
```

---

Promise

- 비동기 작업을 더 체계적으로 다루기 위한 객체

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("완료!");
    // reject('실패!');
  }, 1000);
});

promise
  .then((result) => {
    console.log(result); // 1초 후 "완료!"
  })
  .catch((err) => {
    console.error(err);
  });
```

---

async | await

- promise를 더 깔끔하게 쓰는 방법
- `await`은 비동기 함수의 완료를 기다림 -> 동기처럼 코드 작성 가능

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function run() {
  console.log("시작");
  await wait(1000);
  console.log("1초 경과");
}

run();
// 출력: 시작 → (1초) → 1초 경과
```

- `await`은 반드시 `async`함수 안에서만 사용 가능

---

Event Loop + Call Stack + Callback Queue 구조

- 자바스크립트의는 싱글 스레드 언어인데도 비동기 코드가 잘 작동하는 이유는 브라우저의 이벤트 루프(Event Loop) 구조 덕분임.

1. Call Stack: 현재 실행중인 코드 쌓이는 공간
2. Web APIs: `setTimeout`, `DOM 이벤트`, `fetch`등 브라우저가 처리
3. Callback Queue: 완료된 작업의 콜백이 대기
4. Event Loop: 스택이 비면, 큐에서 콜백 꺼내서 실행
