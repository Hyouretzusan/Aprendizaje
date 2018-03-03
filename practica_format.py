import re

letter = """\nDear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

response = {"salutation" : "Mister", "name" : "H", "product" : "paint", "verbed" : "exploded", "room" : "kitchen", "animals" : "dogs",\
"amount" : "45$", "percent" : "10", "spokesman" : "Mister P", "job_title" : "Wicked salesman"}

print(letter.format(**response))

mammoth = '''We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''


c_words = re.findall(r"\bc\w*", mammoth)
print(c_words)
c4l_words = re.findall(r"\bc\w{3}\b", mammoth)
print(c4l_words)