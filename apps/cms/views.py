from flask import render_template, redirect, url_for
from flask import views, request, session

from apps.cms import cms
from apps.cms.models import CMSUser
from apps.utils import xjson
from config import config


class LoginView(views.MethodView):
    """
    后台
    """

    def get(self):
        return render_template('cms/cms_login.html')

    def post(self):
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        remember = request.form.get('checked')
        cms_user = CMSUser.query.filter_by(username=username).first()
        if cms_user and cms_user.check_password(password):
            session[config['development'].CMS_USER_ID] = cms_user.id
            if remember:
                session.permanent = True
            return xjson.json_success('登陆成功', {'admin': cms_user.username})
        return xjson.json_params_error('用户名或密码错误', {'username': username})


class LogoutView(views.MethodView):
    """
    后台退出
    """

    def get(self):
        session.pop(config['development'].CMS_USER_ID)
        return redirect(url_for('cms.login'))


class IndexView(views.MethodView):
    """
    后台主页
    """

    def get(self):
        return render_template('cms/cms_index.html')


cms.add_url_rule('/login/', view_func=LoginView.as_view('login'))
cms.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))
cms.add_url_rule('/index/', view_func=IndexView.as_view('index'))
