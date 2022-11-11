from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=36,
                            verbose_name='название категории',
                            help_text='36 макс.',
                            null=False, blank=False
                            )
    parent = models.ForeignKey('Category',
                               on_delete=models.CASCADE,
                               verbose_name='родительская категория',
                               null=True, blank=True
                               )
    description = models.CharField(max_length=255,
                                   blank=True, null=True,
                                   verbose_name='описание',
                                   help_text='255 макс.'
                                   )
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация'
                                       )

    def __str__(self):
        return f'Категория: {self.name}'

    class Meta:
        db_table = 'auction_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('is_published', 'name')


class Lot(models.Model):
    name = models.CharField(max_length=36,
                            verbose_name='название лота',
                            help_text='36 макс.',
                            null=False, blank=False
                            )
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 verbose_name='категория лота',
                                 null=True, blank=False
                                 )
    image = models.ImageField(upload_to='images/',
                              null=True, blank=True,
                              verbose_name='изображение'
                              )
    description = models.CharField(max_length=255,
                                   verbose_name='описание лота',
                                   help_text='255 макс.',
                                   null=True, blank=True
                                   )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='владелец',
                              null=False, blank=False
                              )
    created_date = models.DateTimeField(auto_now=False,
                                        auto_now_add=True,
                                        verbose_name='дата добавления',
                                        null=False, blank=False
                                        )

    def __str__(self):
        return f'Лот: {self.name}'

    class Meta:
        db_table = 'auction_lots'
        verbose_name = 'lot'
        verbose_name_plural = 'lots'
        ordering = ('owner', 'created_date')


class Event(models.Model):
    name = models.CharField(max_length=36,
                            verbose_name='имя аукциона',
                            help_text='36 макс.',
                            null=False, blank=False
                            )
    lot = models.ForeignKey('Lot',
                            on_delete=models.PROTECT,
                            verbose_name='лот',
                            null=False, blank=False
                            )
    buyout_price = models.DecimalField(decimal_places=2,
                                       max_digits=10,
                                       verbose_name='цена выкупа $',
                                       help_text='$99999999.99 макс.',
                                       null=True, blank=True
                                       )
    start_price = models.DecimalField(decimal_places=2,
                                      max_digits=10,
                                      verbose_name='стартовая цена $',
                                      help_text='$99999999.99 макс.',
                                      null=False, blank=False
                                      )

    start_date = models.DateTimeField(auto_now=False,
                                      auto_now_add=False,
                                      verbose_name='дата начала'
                                      )
    end_date = models.DateTimeField(auto_now=False,
                                    auto_now_add=False,
                                    verbose_name='дата окончания'
                                    )
    winner = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               verbose_name='победитель',
                               null=True, blank=True
                               )
    is_started = models.BooleanField(verbose_name='начат',
                                     default=False
                                     )
    is_closed = models.BooleanField(verbose_name='окончен',
                                    default=False
                                    )

    def __str__(self):
        return f'Аукцион: {self.name}'

    class Meta:
        db_table = 'auction_events'
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ('start_date', )


class Bet(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             verbose_name='участник',
                             null=False, blank=False
                             )
    event = models.ForeignKey(Event,
                              on_delete=models.PROTECT,
                              verbose_name='аукцион',
                              null=False, blank=False
                              )
    created_date = models.DateTimeField(auto_now=False,
                                        auto_now_add=True,
                                        verbose_name='дата ставки',
                                        null=False, blank=False
                                        )
    bet = models.DecimalField(decimal_places=2,
                              max_digits=10,
                              verbose_name='ставка $',
                              help_text='$99999999.99 макс.',
                              null=False, blank=False
                              )

    def __str__(self):
        return f'Ставка: {self.user} | ${self.bet} | на аукционе - {self.event.name}'

    class Meta:
        db_table = 'auction_bets'
        verbose_name = 'bet'
        verbose_name_plural = 'bets'
        ordering = ('created_date', 'bet')


class FeedBack(models.Model):
    email = models.EmailField(max_length=30, verbose_name="почта")
    message = models.CharField(max_length=140, verbose_name="сообщение")
    created_date = models.DateTimeField(auto_now=False,
                                        auto_now_add=True,
                                        verbose_name="дата обращения"
                                        )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = 'app_feedback'
        ordering = ('created_date', 'email')
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
