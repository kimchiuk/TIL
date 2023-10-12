# Many to one relationships (N:1 or 1:N)

Many to one relationships
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

comment(N) - article(1)
- 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있다.

테이블 관계

![Alt text](image.png)
![Alt text](image-1.png)

ForeignKey()
- N:1 관계 설정 모델 필드

# 댓글 모델 구현

댓글 모델 정의
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
- ForeignKey 클래스를 작성하는 위치와 관계없이 외래 키는 테이블 필드 마지막에 생성됨

```py
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

ForeignKey(to, on_delete) 에서 'to'
- 참조하는 모델 class 이름

ForeignKey(to, on_delete) 에서 'on_delete'
- 왜래 키가 참조하는 객체(1)가 사라졋을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정
  (데이터 무결성)

on_delete의 'CASCADE'
- 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
- 기타 설정 값 참고

Migration
- 댓글 테이블의 article_id 필드 확인
- 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유
  - 참조 대상 클래스 이름 + '_' + '클래스 이름'

# 댓글 생성 연습

댓글 생성 연습
- shell_plus 실행 및 게시글 작성
```py
$ python manage.py shell_plus

# 게시글 생성
Article.objects.create(title='title', content='content')
```

- 댓글 생성
```py
# Comment 클래스의 인스턴스 comment 생성
comment = Comment()

# 인스턴스 변수 저장
comment.content = 'first comment'

# DB에 댓글 저장
comment.save()

# 에러 발생
django.db.utils.IntegrityError: NOT NULL constraint failed:
articles_comment.article_id
# articles_comment 테이블의 ForeignKeyField, article_id 값이 저장 시 누락되었기 때문
```

- shell_plus 실행 및 게시글 작성
```py
# 게시글 조회
article = Artticle.objects.get(pk=1)

# 외래 키 데이터 입력
comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에 
# 넣어 줄 수도 있지만 권장하지 않음

# 댓글 저장 및 확인
comment.save()
```

- comment 인스턴스를 통한 article 값 참조하기
```py
comment.pk
=> 1

comment.content
=> 'first comment'

# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
comment.article
=> <Article: Article object (1)>

# article_pk는 존재하지 않는 필드이기 때문에 사용 불가
comment.article_id
=> 1
```

- shell_plus 실행 및 게시글 작성
```py
# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1

# 1번 댓글이 작성된 게시물의 comment 조회
comment.article.comment
=> 'content'
```

- 두번째 댓글 작성
```py
comment = Comment(content='second comment', article=article)
comment.save()

comment.pk
=> 2

comment
=> <Comment: Comment object (2)>

comment.article.pk
=> 1
```

- 작성된 댓글 데이터 확인


# 관계 모델 참조

역참조
- N:1 관계에서 1에서 N을 참조하거나 조회하는 것
  1 -> N

- > N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요

역참조 사용 예시
- article.comment_set.all()
- 모델인스턴스.related manager(역참조 이름).QuerySet API

related manager
- N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저

- > 'objects' 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨

related manager 이름 규칙
- N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐
- 해당 댓글의 게시글 (comment -> Article)
  - comment.article
- 게시글의 댓글 목록 (Article -> Comment)
  - article.comment_set.all()

Related manager 연습
- shell_plus 실행 및 1번 게시글 조회
```py
$ python manage.py shell_plus

article = Article.object.get(pk=1)
```

- 1번 게시글에 작성된 모든 댓글 조회하기 (역참조)
```py
>>> article.comment_set.all()
<QuerySet [<Comment: Comment object (1)>,
<Comment: Comment object (2)>]>
```

- 1번 게시글에 작성된 모든 댓글 내용 출력
```py
comment = article.comment_set.all()

for comment in comments:
    print(comment.content)
```

# 댓글 구현
## 댓글 create

댓글 CREATE 구현
- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 정의
```py
# articles/forms.py

from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```

- detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링
```py
# articles/views.py

from .forms import ArticleForm, CommentForm


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- articles/detail.html -->

<form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

- Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요한 필드이기 떄문에 출력 되고 있는 것
- 하지만, 외래 키 필드는 사용자 입력 값으로 받는 것이 아닌 view 함수 내에서 다른 방법으로 전달 받아 저장되어야 함

- CommentForm의 출력 필드 조정
```py
# articles/forms.py

from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```

- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?
- detail 페이지의 url
  path('<int:pk>/', views.detail, name='detail')에서 해당 게시글 pk 값이 사용 되고 있음
- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

- url 작성 및 action 값 작성
```py
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```html
<!-- articles/detail.html -->

<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

- comments_create view 함수 정의 
  - > article 객체는 언제 저장할 수 있을까?
```py
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

save(commit=False)
- DB에 저장하지 않고 인스턴스만 반환
  (Create, but don't save the new instance.)

- save의 commit 인자를 활용해 외래 키 데이터 추가 입력
```py
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        retrun diredirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- 댓글 작성 후 테이블 확인

## 댓글 READ

댓글 READ 구현
- detail view 함수에서 전체 댓글 데이터를 조회
```py
# aritlces/views.py

from .models import Article, Comment

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comment = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

- 전체 댓글 출력 및 확인
```html
<!-- articles/detail.html -->

<h4>댓글목록</h4>
<ul>
    {% for comment in comments %}
        <li>{{ comment.content }}</li>
    {% endfor %}
</ul>
```

## 댓글 DELETE

댓글 DELETE 구현
- 댓글 삭제 url 작성
```py
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name='comments_delete'
    ),
]
```

- 댓글 삭제 view 함수 정의
```py
# articles/views.py

from .models import Article, Comment

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

- 댓글 삭제 버튼 작성
```html
<!-- articles/detail.html -->

<ul>
    {% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
        </form>
    </li>
    {% endfor %}
</ul>
```

- 댓글 삭제 버튼 출력 확인 및 삭제 테스트

# 참고

admin site 등록
- Comment 모델을 admin site에 등록해 CRUD 동작 확인하기

```py
# articles/admin.py

from .model import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

댓글이 없는 경우 대체 콘텐츠 출력
- DTL 'for empth' 태그 사용
```html
<!-- articles/detail.html -->

{% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
        </form>
    </li>
{% empty %}
    <p>댓글이 없어요..</p>
{% endfor %}
```

댓글 개수 출력하기
- DTL filter - 'length' 사용
```html
{{ comment|length }}

{{ article.comment_set.all|length }}
```
- Queryset API - 'count()' 사용
```html
{{ article.comment_set.count }}
```

