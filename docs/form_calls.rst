

First Call
-----------

[12/Jul/2015 09:45:16] DEBUG [quiz.views:386] **** DISPATCH ****
[12/Jul/2015 09:45:17] DEBUG [quiz.views:407] **** GET ****
[12/Jul/2015 09:45:17] DEBUG [quiz.views:413] **** GET_FORM ****
[12/Jul/2015 09:45:17] DEBUG [quiz.views:426] **** GET_FORM_KWARGS ****
[12/Jul/2015 09:45:17] DEBUG [quiz.forms:9] *** QuestionForm.__init__ ***
[12/Jul/2015 09:45:17] DEBUG [quiz.views:452] **** GET_CONTEXT_DATA ****


Second Call
-------------


[12/Jul/2015 08:00:41] DEBUG [quiz.views:386] **** DISPATCH ****
[12/Jul/2015 08:00:42] DEBUG [quiz.views:402] **** GET_FORM ****
[12/Jul/2015 08:00:42] DEBUG [quiz.views:415] **** GET_FORM_KWARGS ****
[12/Jul/2015 08:00:42] DEBUG [quiz.forms:9] *** QuestionForm.__init__ ***
[12/Jul/2015 08:00:42] DEBUG [quiz.views:421] **** FORM_INVALID ****
[12/Jul/2015 08:00:42] DEBUG [quiz.views:424] [('Answers', ['Select a valid choice. 2 is not one of the available choices.'])]
[12/Jul/2015 08:00:42] DEBUG [quiz.views:441] **** GET_CONTEXT_DATA ****


3rd Call
------------

[12/Jul/2015 08:03:04] DEBUG [quiz.views:386] **** DISPATCH ****
[12/Jul/2015 08:03:04] DEBUG [quiz.views:402] **** GET_FORM ****
[12/Jul/2015 08:03:04] DEBUG [quiz.views:415] **** GET_FORM_KWARGS ****
[12/Jul/2015 08:03:04] DEBUG [quiz.forms:9] *** QuestionForm.__init__ ***
[12/Jul/2015 08:03:04] DEBUG [quiz.views:428] **** FORM_VALID ****
[12/Jul/2015 08:03:04] DEBUG [quiz.views:475] **** FORM_VALID_USER ****