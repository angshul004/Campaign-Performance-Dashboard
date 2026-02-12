from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from .extensions import db
from .models import Campaign

main = Blueprint("main", __name__)


@main.route("/")
def home():
    campaign_list = Campaign.query.order_by(Campaign.id.desc()).all()

    total_campaigns = len(campaign_list)
    total_leads = sum(c.leads for c in campaign_list)
    total_conversions = sum(c.conversions for c in campaign_list)

    platform_totals = {}
    for campaign in campaign_list:
        platform_totals[campaign.platform] = platform_totals.get(campaign.platform, 0) + campaign.conversions

    top_platform = max(platform_totals, key=platform_totals.get) if platform_totals else "N/A"
    recent_campaigns = campaign_list[:5]

    return render_template(
        "home.html",
        total_campaigns=total_campaigns,
        total_leads=total_leads,
        total_conversions=total_conversions,
        top_platform=top_platform,
        recent_campaigns=recent_campaigns,
    )


@main.route("/add")
def add_campaign():
    return render_template("add_campaign.html")


@main.route("/add", methods=["POST"])
def create_campaign():
    start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d").date()
    end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d").date()

    campaign = Campaign(
        campaign_name=request.form["campaign_name"],
        platform=request.form["platform"],
        budget=float(request.form["budget"]),
        impressions=int(request.form["impressions"]),
        clicks=int(request.form["clicks"]),
        leads=int(request.form["leads"]),
        conversions=int(request.form["conversions"]),
        start_date=start_date,
        end_date=end_date,
    )
    db.session.add(campaign)
    db.session.commit()

    return redirect(url_for("main.campaigns"))


@main.route("/campaigns")
def campaigns():
    campaign_list = Campaign.query.order_by(Campaign.id.desc()).all()
    return render_template("campaigns.html", campaigns=campaign_list)


@main.route("/dashboard")
def dashboard():
    campaign_list = Campaign.query.order_by(Campaign.id.asc()).all()

    total_campaigns = len(campaign_list)
    total_leads = sum(c.leads for c in campaign_list)
    total_conversions = sum(c.conversions for c in campaign_list)
    conversion_rate = (total_conversions / total_leads * 100) if total_leads else 0

    campaign_labels = [c.campaign_name for c in campaign_list]
    clicks_data = [c.clicks for c in campaign_list]
    conversions_data = [c.conversions for c in campaign_list]

    platform_totals = {}
    for campaign in campaign_list:
        platform_totals[campaign.platform] = platform_totals.get(campaign.platform, 0) + campaign.conversions

    platform_labels = list(platform_totals.keys())
    platform_data = list(platform_totals.values())

    return render_template(
        "dashboard.html",
        total_campaigns=total_campaigns,
        total_leads=total_leads,
        total_conversions=total_conversions,
        conversion_rate=conversion_rate,
        campaign_labels=campaign_labels,
        clicks_data=clicks_data,
        conversions_data=conversions_data,
        platform_labels=platform_labels,
        platform_data=platform_data,
    )
