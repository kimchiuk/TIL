# form

HTML 'form'
- 지금까지 사용자로부터 데이터를 받기위해 활용한 방법
  그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
  
  -> 유효한 데이터인지에 대한 확인이 필요

유효성검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정

유효성 검사 구현
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용


# Django Form

- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

-> 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

Form class 정의
```python
# articles/forms.py

from Django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.charField()
```

Form class를 적용한 new 로직
```python
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'article/new.html', context)

```

```html
<!-- articles/new.html -->

<h1>NEW</h1>
<form action="{% url 'articles:create' %}>" method="POST">
    {% csrf token %}
    {{ form }}
    <input type="submit">
</form>
```

Form rendering options
- label, input 쌍을 특정 HTML 태그로 감싸는 옵션
```html
<!-- articles/new.html -->

<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```

# Widgets

- HTML 'input' element의 표현을 담당

widget 사용
- widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

# django modelform

Form : 사용자 입력 데이터를 DB에 저장하지 않을 떄(ex. 로그인)

modelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글, 회원가입)

ModelForm
- model과 연결된 Form을 자동으로 생성해주는 기능을 제공

-> Form + Model

ModelForm class 정의
- 기존 ArticleForm 클래스 수정
```python
# articles/forms/py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

Meta calss
- ModelForm의 정보를 작성하는 곳

'fields' 및 'exclude' 속성
- exclude 속성을 사용하여 모델에서 포함하지 않을필드를 지정할 수도 있음

```python
# articles/forms/py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)
```

```python
# articles/forms/py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('title',)
```

ModelForm을 적용한 create 로직
```python
# articles/views.py

from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

ModelForm을 적용한 create 로직
- 제목 input에 공백을 입력 후 에러 메시지를 출력 확인 (유효성 검사의 결과)

is_valid()
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 변환

공백 데이터가 유효하지 않은 이유와 에러메시지가 출력되는 과정
- 별도로 명시하지는 않았지만 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정되어있음
- 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context) 
```

ModelForm을 적용한 edit 로직
```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->

<h1>EDIT</h1>
<form action="{% 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>

```

ModelForm을 적용한 update 로직

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

save()
- 데이터베이스 객체를 만들고 저장

save() 메서드가 생성과 수정을 구분하는 법
- 키워드 인자 instance 여부를 생성할 지, 수정할 지를 결정

```python
# CREATE
form = ArticleForm(request.POST)
form.save()

# UPDATE
form = ArticleForm(request.POST, instance=article)
form.save()
```

Django Form 정리
- "사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유현한 도구"
  HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움


# 참고

ModelForm 키워드 인자 data와 instance 살펴보기
```py
class BaseModelForm(BaseForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
```

Widget 응용
```py
# articles/forms.py

class ArticleForm(form.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
```

```py
class ArticleForm(form.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    context = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )
```

# Handling HTTP requests

## view 함수 구조 변화

new & create view 함수간 공통점과 차이점

- 공통점 : '데이터 생성을 구현하기 위함'

- 차이점 : 'new는 GET method 요청만을, create는 POST method 요청만을 처리'


HTTP request method 차이점을 활용해 view 함수 구조 변경

new & create 함수 결합
```py
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```


```py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        context = {
            'form': form,
        }
    }
    return render(request, 'articles/new.html', context)
```

새로운 create view 함수
- new와 create view 함수의 공통점과 차이점을 기반으로 하나의 함수로 결합
```py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'aritcles/new.html', context)
```

- 두 함수위 유일한 차이점이었던 request method에 따른 분기

- POST일 때는 create 함수 구조였던 객체 생성 및 저장 로직 처리

- POST가 아닐 때는 과거 단순히 form 인스턴스 생성

- context에 담기는 form은
1. is_valid를 통과하지 못해 에러메시지를 담은 form이거나
2. else 문을 통한 form 인스턴스

기존 new 관련 코드 수정
- 사용하지 않는 new url 제거

```py
# articles/views.py

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

- new url을 create url로 변경

- new 템플릿을 create 템플릿으로 변경


request method에 따른 요청의 변화

- (GET) articles/create/    게시글 생성 문서를 줘!

- (POST) articles/create/   게시글을 생성해줘!


새로운 update view 함수
- 기존 edit과 update view 함수 결합
```py
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method== 'POST':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

기존 edit 관련 코드 수정
- 사용하지 않는 edit url 제거
```py
# articles/views.py

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

- edit 템플릿을 update 템플릿으로 변경

