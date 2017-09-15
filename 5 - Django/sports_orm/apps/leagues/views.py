from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	# Level 1
		# 1) League.objects.filter(sport="Baseball")
		# 2) League.objects.filter(name__contains="Women")
		# 3) League.objects.filter(sport__contains="Hockey")
		# 4) League.objects.exclude(sport="Football")
		# 5) League.objects.filter(name__contains="Conference")
		# 6) League.objects.filter(name__contains="Atlantic")
		# 7) Team.objects.filter(location="Dallas")
		# 8) Team.objects.filter(team_name__contains="Raptors")
		# 9) Team.objects.filter(location__contains="City")
		# 10) Team.objects.filter(team_name__startswith="T")
		# 11) Team.objects.order_by('location')
		# 12) Team.objects.order_by('-location')
		# 13) Player.objects.filter(last_name="Cooper")
		# 14) Player.objects.filter(first_name="Joshua")
		# 15) Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
		# 16) Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
	#Level 2
		# 1) Team.objects.filter(league__name="Atlantic Soccer Conference")
		# 2) Player.objects.filter(curr_team__team_name="Penguins")
		# 3) Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")
		# 4) Player.objects.filter(curr_team__league__name="American Conference of Amateur Football")
		# 5) Player.objects.filter(all_teams__league__sport="Football")
		# 6) Team.objects.filter(curr_players__first_name="Sophia")
		# 7) League.objects.filter(teams__curr_players__first_name="Sophia")
		# 8) Player.objects.exclude(last_name="Flores", curr_team__team_name="RoughRiders")
		# 9) Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans")
		# 10) Player.objects.filter(all_teams__team_name="Tiger-Cats")
		# 11) Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings")
		# 12) Team.objects.filter(all_players__first_name="Jacob").filter(all_players__last_name="Gray").exclude(curr_players__first_name="Jacob").exclude(curr_players__last_name="Gray")
		# 13) Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
		# 14)
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
