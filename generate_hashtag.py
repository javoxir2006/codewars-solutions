# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"

def generate_hashtag(s):
    tag = "#"
    if not s:
        return False
    x = []
    m = s.lower()
    m = s.title()
    x = m.split()
    for i in x:
        tag+=i
    if len(tag) > 140:
        return False
    return tag
