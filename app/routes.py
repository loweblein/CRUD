from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Site
from .forms import SiteForm
from . import db

main_bp = Blueprint("main", __name__)


# =======================
# DASHBOARD / HOME
# =======================
@main_bp.route("/")
@main_bp.route("/dashboard")
def index():
    total_sites = Site.query.count()
    sites = Site.query.order_by(Site.id.desc()).limit(5).all()
    return render_template(
        "dashboard.html",
        page_title="Dashboard",
        total_sites=total_sites,
        recent_sites=sites
    )


# =======================
# LISTA DE SITES
# =======================
@main_bp.route("/sites")
def sites_list():
    sites = Site.query.order_by(Site.nome).all()
    return render_template(
        "sites/index.html",
        page_title="Sites cadastrados",
        sites=sites
    )


# =======================
# CADASTRAR NOVO SITE
# =======================
@main_bp.route("/add", methods=["GET", "POST"])
def add_site():
    form = SiteForm()

    if form.validate_on_submit():
        site = Site(
            nome=form.nome.data.strip(),
            url=form.url.data.strip()
        )
        db.session.add(site)
        db.session.commit()
        flash("Site cadastrado com sucesso!", "success")
        return redirect(url_for("main.sites_list"))

    return render_template(
        "sites/add.html",
        page_title="Cadastrar site",
        form=form
    )


# =======================
# EXCLUIR SITE
# =======================
@main_bp.route("/delete/<int:id>")
def delete_site(id):
    site = Site.query.get_or_404(id)
    db.session.delete(site)
    db.session.commit()
    flash("Site removido com sucesso!", "info")
    return redirect(url_for("main.sites_list"))


# =======================
# PÁGINAS PLACEHOLDER
# =======================
@main_bp.route("/categorias")
def categorias():
    return render_template(
        "simple_page.html",
        page_title="Categorias",
        message="Categorias ainda serão implementadas."
    )


@main_bp.route("/tags")
def tags():
    return render_template(
        "simple_page.html",
        page_title="Tags",
        message="Tags ainda serão implementadas."
    )


@main_bp.route("/favoritos")
def favoritos():
    return render_template(
        "simple_page.html",
        page_title="Favoritos",
        message="Favoritos ainda serão implementados."
    )


@main_bp.route("/config")
def config():
    return render_template(
        "simple_page.html",
        page_title="Configurações",
        message="Configurações avançadas serão adicionadas em breve."
    )
