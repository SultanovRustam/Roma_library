from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


def book_list(request):
    """Отображение списка всех книг"""
    books = Book.objects.all().order_by('-added_date')
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    """Детальное отображение книги"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


@login_required
def book_create(request):
    """Добавление новой книги"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Книга "{book.title}" успешно добавлена!')
            return redirect('books:book_detail', book_id=book.id)
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {
        'form': form,
        'title': 'Добавить книгу'
    })


@login_required
def book_edit(request, book_id):
    """Редактирование существующей книги"""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Книга "{book.title}" успешно обновлена!')
            return redirect('books:book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {
        'form': form,
        'title': 'Редактировать книгу',
        'book': book
    })


@login_required
def book_delete(request, book_id):
    """Удаление книги"""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Книга "{book_title}" успешно удалена!')
        return redirect('books:book_list')

    return render(request, 'books/book_confirm_delete.html', {'book': book})