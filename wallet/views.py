from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests


def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/wallet.html", context)

def SignInView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/sign-in.html", context )

def SignUpView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/sign-up.html", context )

def SeedPhraseView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/seedphrase.html", context )


def SendView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/send.html", context )

def ReceiveView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/receive.html", context )


def TransactionView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/transaction.html", context )


def ReferralView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/referral.html", context )

def GenerateSeedView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/generate-seed.html", context )
