#encoding:utf-8

subreddit = 'DeepFriedMemes'
t_channel = '@r_DeepFriedMemes'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
