from datetime import timedelta
from dateutil.parser import parse
import random

from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
import xgboost as xgb

from .models import Price, User, Account, Transaction, Node


LOGIN_URL = "/admin/"


@login_required(login_url=LOGIN_URL)
def trade(
    request: HttpRequest,
    start: str = "2023-01-01",
    end: str = "2023-01-02",
    node: str = "MILPITAS_1_N008",
):
    prices = Price.objects.filter(
        node=Node.objects.filter(name=node).get(),
        start__gte=parse(start),
        end__lte=parse(end) + timedelta(days=1),
    ).all()
    predicts = Price.objects.filter(
        node=Node.objects.filter(name=node).get(),
        start__gt=parse(end),
        end__lte=parse(end) + timedelta(days=1),
    ).all()
    moving_averages = []
    for p in predicts:
        moving_averages.append(p.rtm)
        if p.start.minute == 0:
            p.rtm = 0.1 * p.rtm + 0.9 * (sum(moving_averages) / len(moving_averages))
            p.end = p.start + timedelta(hours=1)
        else:
            p.rtm = None
        if len(moving_averages) > 50:
            moving_averages.pop(0)
    context = {
        "prices": prices,
        "predicts": predicts,
        "start": start,
        "end": end,
        "node": node,
        "nodes": Node.objects.exclude(name=node).all(),
        "skips": range(
            len(
                Price.objects.filter(
                    node=Node.objects.filter(name=node).get(),
                    start__gte=parse(start),
                    end__lte=parse(end),
                ).all()
            ) + 1
        ),
    }
    return render(request, "predict/index.html", context)


@login_required(login_url=LOGIN_URL)
def balance(request: HttpRequest):
    if not Account.objects.filter(user=request.user).exists():
        a = Account(user=request.user, balance=10000)
        a.save()
    context = {
        "user": request.user,
        "transactions": Transaction.objects.filter(user=request.user).all(),
    }
    return render(request, "predict/balance.html", context)


@login_required(login_url=LOGIN_URL)
def predict(request: HttpRequest):
    context = {}
    return render(request, "predict/index.html", context)


@login_required(login_url=LOGIN_URL)
def daily(
    request: HttpRequest,
    start: str = "2023-01-01",
    end: str = "2023-01-02",
    node: str = "MILPITAS_1_N008",
):
    prices = Price.objects.filter(
        node=Node.objects.filter(name=node).get(),
        start__gte=parse(start),
        end__lte=parse(end) + timedelta(days=1),
    ).all()
    predicts = Price.objects.filter(
        node=Node.objects.filter(name=node).get(),
        start__gt=parse(end),
        end__lte=parse(end) + timedelta(days=1),
    ).all()
    moving_averages = []
    for p in predicts:
        moving_averages.append(p.rtm)
        if p.start.minute == 0:
            p.rtm = 0.1 * p.rtm + 0.9 * (sum(moving_averages) / len(moving_averages))
            p.end = p.start + timedelta(hours=1)
        else:
            p.rtm = None
        if len(moving_averages) > 50:
            moving_averages.pop(0)
    context = {
        "prices": prices,
        "predicts": predicts,
        "start": start,
        "end": end,
        "node": node,
        "nodes": Node.objects.exclude(name=node).all(),
        "skips": range(
            len(
                Price.objects.filter(
                    node=Node.objects.filter(name=node).get(),
                    start__gte=parse(start),
                    end__lte=parse(end),
                ).all()
            ) + 1
        ),
    }
    return render(request, "predict/daily.html", context)


@login_required(login_url=LOGIN_URL)
def home(request: HttpRequest):
    nodes = Node.objects.all()
    context = {
        "nodes": nodes,
        "online_users": random.randint(10, 100),
        "total_users": random.randint(100, 1000),
        "subscribed_users": random.randint(100, 200),
        "num_nodes": len(nodes),
    }
    return render(request, "predict/home.html", context)