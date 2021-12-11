from django import template

register = template.Library()


@register.filter(name='comment_amount')
def comment_amount(NUMCOMMENTS):
    if NUMCOMMENTS == 0:
        return 'nenhum comentário'
    elif NUMCOMMENTS == 1:
        return '1 comentário'
    else:
        return f'{NUMCOMMENTS} comentários'
