from django.shortcuts import render, redirect

def login_view(request):
    hardcoded_pin = "1234"
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if pin == hardcoded_pin:
            request.session['balance'] = 0  # Initialize balance in session
            return redirect('dashboard')
        else:
            return render(request, 'atm/login.html', {'error': 'Invalid PIN'})
    return render(request, 'atm/login.html')

def dashboard_view(request):
    return render(request, 'atm/dashboard.html')

def balance_view(request):
    balance = request.session.get('balance', 0)
    return render(request, 'atm/balance.html', {'balance': balance})

def deposit_view(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        request.session['balance'] = request.session.get('balance', 0) + amount
        return redirect('balance')
    return render(request, 'atm/deposit.html')

def withdraw_view(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        balance = request.session.get('balance', 0)
        if amount > balance:
            return render(request, 'atm/withdraw.html', {'error': 'Insufficient funds'})
        else:
            request.session['balance'] = balance - amount
            return redirect('balance')
    return render(request, 'atm/withdraw.html')