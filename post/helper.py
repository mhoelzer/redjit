from redjit.comment.models import Comment



def toggle_comment_upvotes(request):
    if 'upvote' in request.POST:
        comment = Comment.objects.get(id=request.POST['upvote'])
        if request.user.redjiter in comment.upvotes.all():
            comment.upvotes.remove(request.user.redjiter)
        else: 
            comment.downvotes.remove(request.user.redjiter)
            comment.upvotes.add(request.user.redjiter)

    if 'downvote' in request.POST:
        comment = Comment.objects.get(id=request.POST['downvote'])
        if request.user.redjiter in comment.downvotes.all():
            comment.downvotes.remove(request.user.redjiter)
        else: 
            comment.upvotes.remove(request.user.redjiter)
            comment.downvotes.add(request.user.redjiter)
        comment.save()
    return

def sort_comments(comments):
    sorted_comments = sorted(comments, reverse=True, key=lambda comment: comment.get_score())
    return sorted_comments