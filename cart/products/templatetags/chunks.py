from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk
            chunk=[] ##reset chunk
            i=0##resets the counter for the new chunk.
    if chunk:## If there are remaining items in the last chunk, yield it
        yield chunk 