Problem 1-1. Solving recurrences
Derive solutions to the following recurrences in two ways: via a recursion tree and via Master
Theorem. A solution should include the tightest upper and lower bounds that the recurrence will
allow. Assume T(1) ∈ Θ(1).

> (a) T(n) = 2 T(n/2) + O(n)
> 마스터 정리에 의해 O(n)
> (b) T(n) = 8 T(n/4) + O(n root(n))
> 마스터 정리에 의해 O(n^3/2\*log2n)
> (c) T(n) = T(n/3) + T(n/4) + Θ(n) assuming T(a) < T(b) for all a < b
> 마스터 정리 사용불가, O(n^2 log n)

Problem 1-2. Stone Searching
Sanos is a supervillain on an intergalactic quest in search of an ancient and powerful artifact called
the Thoul Stone. Unfortunately she has no idea what planet the stone is on. The universe is
composed of an infinite number of planets, each identified by a unique positive integer. On each
planet is an oracle who, after some persuasion, will tell Sanos whether or not the Thoul Stone
is on a planet having a strictly higher planet identifier than their own. Interviewing every oracle
in the universe would take forever, and Sanos wants to find the Thoul Stone quickly. Supposing
the Thoul Stone resides on planet k, describe an algorithm to help Sanos find the Thoul Stone by
interviewing at most O(log k) oracles.

> 이진 탐색을 통해 log 의 시간으로 행성 k 를 찾을 수 있음

Problem 1-3. Collage Collating
Fodoby is a company that makes customized software tools for creative people. Their newest
software, Ottoshop, helps users make collages by allowing them to overlay images on top of each
other in a single document. Describe a database to keep track of the images in a given document
which supports the following operations:

1. make document(): construct an empty document containing no images
2. import image(x): add an image with unique integer ID x to the top of the document
3. display(): return an array of the document’s image IDs in order from bottom to top
4. move below(x, y): move the image with ID x directly below the image with ID y
   Operation (1) should run in worst-case O(1) time, operations (2) and (3) should each run in worstcase O(n) time, while operation (4) should run in worst-case O(log n) time, where n is the number
   of images contained in a document at the time of the operation.

> 더블 링크드 리스트

Problem 1-4. Brick Blowing
Porkland is a community of pigs who live in n houses lined up along one side of a long, straight
street running east to west. Every house in Porkland was built from straw and bricks, but some
houses were built with more bricks than others. One day, a wolf arrives in Porkland and all the
pigs run inside their homes to hide. Unfortunately for the pigs, this wolf is extremely skilled at
blowing down pig houses, aided by a strong wind already blowing from west to east. If the wolf
blows in an easterly direction on a house containing b bricks, that house will fall down, along with
every house east of it containing strictly fewer than b bricks. For every house in Porkland, the wolf
wants to know its damage, i.e., the number of houses that would fall were he to blow on it in an
easterly direction.
(a) Suppose n = 10 and the number of bricks in each house in Porkland from west to east
is [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]. Compute for this instance the
damage for every house in Porkland.

> 34 - 4개, 57 - 5개, 70 - 6개, 19 - 3개, 48 - 3개, 2 - 1개, 94 - 4개, 7 - 1개, 63 - 1개, 75 - 1개

(b) A house in Porkland is special if it either (1) has no easterly neighbor or (2) its adjacent neighbor to the east contains at least as many bricks as it does. Given an array
containing the number of bricks in each house of Porkland, describe an O(n)-time
algorithm to return the damage for every house in Porkland when all but one house
in Porkland is special.

>

(c) Given an array containing the number of bricks in each house of Porkland, describe
an O(n log n)-time algorithm to return the damage for every house in Porkland.
(d) Write a Python function get damages that implements your algorithm.
