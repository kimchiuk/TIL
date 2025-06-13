### react 상태관리

---
1. useState / useReducer

- 컴포넌트 내부의 간단한 UI 상태 (토글, 입력값 등)
- useReducer는 복잡한 로직/상태 분기에 적합


useState 예시

```js
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>증가</button>
    </>
  );
}
```

useReducer 예시

```js
import { useReducer } from 'react';

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': return { count: state.count + 1 };
    default: return state;
  }
};

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>증가</button>
    </>
  );
}
```

- 가볍고 빠르며 의존성이 없는 것이 장점이다.
- 상태공유가 어렵다는 단점이 있다. (부모 -> 자식 단방향 전달만 가능)


---

2. context API

- 전역적으로 공유해야 할 간단한 상태 (예: 다크모드, 언어 설정)에 사용

```js
// ThemeContext.js
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext);
```


```js
// App.js
import { ThemeProvider, useTheme } from './ThemeContext';

function ThemedComponent() {
  const { theme, setTheme } = useTheme();
  return <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>{theme}</button>;
}

function App() {
  return (
    <ThemeProvider>
      <ThemedComponent />
    </ThemeProvider>
  );
}


```

- 전역상태에서 공유 가능하다
- 리렌더링 이슈가 발생한다. (모든 하위 컴포넌트에)
- 성능 최적화가 필요하다

---

3. zustand

- 작고 빠르며 Context보다 성능이 좋고 사용이 간편한 전역 상태관리 라이브러리이다.
- 간단하고 빠른 전역상태 공유
- Recoil보다 가볍고 성능 지향

```bash
npm i zustand
```
```js
// store.js
import { create } from 'zustand';

export const useStore = create((set) => ({
  count: 0,
  increase: () => set((state) => ({ count: state.count + 1 })),
}));
```
```js
// App.js
import { useStore } from './store';

function Counter() {
  const { count, increase } = useStore();
  return (
    <>
      <p>{count}</p>
      <button onClick={increase}>증가</button>
    </>
  );
}

```

- 사용법이 매우 간단하며 성능이 우수하다. (불필요한 리렌더링을 방지한다)
- middle ware 활용 가능하다. (persist, devtools)
- 복잡한 비동기 흐름처리에는 제한적이라는 단점이 있다.


--- 

4. Recoil
- Facebook이 만든 전역상태관리 라이브러리로 React 친화적이며 비동기 처리에 강하다.
- 비동기 전역상태(서버 상태 캐싱, 비동기 의존성)

```bash
npm install recoil
```
```js
// atoms.js
import { atom } from 'recoil';

export const countAtom = atom({
  key: 'countAtom',
  default: 0,
});

```

```js
// App.js
import { RecoilRoot, useRecoilState } from 'recoil';
import { countAtom } from './atoms';

function Counter() {
  const [count, setCount] = useRecoilState(countAtom);
  return (
    <>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>증가</button>
    </>
  );
}

function App() {
  return (
    <RecoilRoot>
      <Counter />
    </RecoilRoot>
  );
}
```

- 비동기 셀렉터, 의존성 관리가 탁월하다.
- 성능이 우수하다
- 러닝 커브가 존재한다.
- 상태 디버깅이 어려울 수 있다.


--- 

5. Redux / Redux Toolkit

- 대규모 애플리케이션의 상태관리에 적합한 가장 유명한 라이브러리
- 복잡한 비즈니스 로직, 상태 변경 추적이 필요한 프로젝트에 사용한다

```bash
npm install @reduxjs/toolkit react-redux
```
```js
// store.js
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; }
  },
});

export const { increment } = counterSlice.actions;

export const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});
```
```js
// App.js
import { Provider, useSelector, useDispatch } from 'react-redux';
import { store, increment } from './store';

function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();
  return (
    <>
      <p>{count}</p>
      <button onClick={() => dispatch(increment())}>증가</button>
    </>
  );
}

function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}
```

- 철저한 구조화
- 개발자 도구 및 미들웨어 활용 풍부
- 보일러플레이트 코드가 많다. (전혀 변형 없이 여러 군데에서 반복되는 코드 섹션)
- 러닝커브가 존재한다

