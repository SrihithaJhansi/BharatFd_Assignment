from django.db import models
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = models.TextField(blank=True, null=True)    # Hindi translation
    answer_bn = models.TextField(blank=True, null=True)    # Bengali translation

    def save(self, *args, **kwargs):
        # Automatically translate question and answer to Hindi and Bengali
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question

    def get_translated_answer(self, lang):
        if lang == 'hi' and self.answer_hi:
            return self.answer_hi
        elif lang == 'bn' and self.answer_bn:
            return self.answer_bn
        return self.answer

    def __str__(self):
        return self.question