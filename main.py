from flask import Flask, render_template, request, redirect, jsonify, session
import setuptest as ST
from datetime import date, datetime
import metadata as metadatafile

app = Flask(__name__)

app.secret_key = metadatafile.generate_code(15)

databaseHandler = ST.generalDatabase()


@app.route('/login', methods=['POST', 'GET'])
def homePage():
  if request.method == "POST":
    if request.form['form_type'] == 'signup':
      users = []
      for i in databaseHandler.get_data(
          ST.query_list['common_query']['select_query'].format(
              tablename='users')):
        users.append(i[1])
      if request.form['new_username'] in users:
        return render_template('/signup.html', error='user already exists')
      else:
        databaseHandler.Insert_data(
            ST.query_list['user_table']['insert_query'].format(
                username=request.form['new_username'],
                password=request.form['new_password']))
      return redirect('/login')

    else:
      users = []
      for i in databaseHandler.get_data(
          ST.query_list['common_query']['select_query'].format(
              tablename='users')):
        users.append(i[1])
      if request.form['username'] in users:
        if request.form['password'] == databaseHandler.get_data(
            metadatafile.query['user_password'].format(
                tablename='users', username='mohit'))[0][0]:
          session['username'] = request.form['username']
          return redirect('/')
        else:
          return render_template('signup.html', error='password is wrong')
      else:
        return render_template('signup.html', error='user does not exists')
      return request.form

  return render_template('signup.html', error='')


@app.route('/', methods=['POST', 'GET'])
def user_dashboard():
  if 'username' in session:
    if request.method == "POST":
      session.pop('username')
      return redirect('/')
    return render_template('dashbord.html',
                           dashboard_options=metadatafile.Dashboard_options,
                           username=session['username'])
  return redirect('/login')


@app.route('/notepad', methods=['GET', 'POST'])
def notepad_page():
  if 'username' in session:
    if request.method == "POST":
      if 'delete' in request.form:
        databaseHandler.delete_record(
            ST.query_list['common_query']['delete_query'].format(
                id=request.form['delete'], tablename="notepad_table"))
        return redirect('/notepad')
      elif 'update' in request.form:
        id = request.form['update']
        return redirect(f'/notepad/update/{id}')
      return request.form
    data = databaseHandler.get_data(
        ST.query_list['common_query']['special_select'].format(
            tablename='notepad_table', user=session['username']))
    return render_template('notepad_page.html', user_notes=data)
  return redirect('/login')


@app.route('/notepad/update/<id>', methods=["POST", "GET"])
def update_note_page(id):
  if 'username' in session:
    if request.method == "POST":
      if 'update_id' in request.form:
        databaseHandler.update_value(
            ST.query_list['notepad_page']['update_query'].format(
                heading=request.form['note-title'],
                content=request.form['note-content'],
                id=request.form['update_id']))
        return redirect('/notepad')
    data = databaseHandler.get_single(
        ST.query_list['common_query']['singe_record_query'].format(
            id=id, tablename='notepad_table'))
    return render_template('new_note_editor_page.html', existing_data=data)
  return redirect('/login')


@app.route('/add_note', methods=['GET', 'POST'])
def new_note_page():
  if 'username' in session:
    if request.method == 'POST':
      databaseHandler.Insert_data(
          ST.query_list['notepad_page']['insert_query'].format(
              heading=request.form['note-title'],
              content=request.form['note-content'],
              user=session['username']))
      return redirect('/notepad')
    return render_template('new_note_editor_page.html',
                           existing_data=[['', '', '', '']])
  return redirect('/login')


@app.route('/list', methods=['GET', 'POST'])
def list_page():
  return render_template('list_page.html')


@app.route('/cash_manager', methods=['GET', 'POST'])
def cash_manager_page():
  return render_template('cash_manager_page.html')


@app.route('/webpage_link', methods=['GET', 'POST'])
def webpage_link_page():
  if 'username' in session:
    if request.method == 'POST':
      if 'delete' in request.form:
        databaseHandler.delete_record(
            ST.query_list['website_link_page']['delete_query'].format(
                id=request.form['delete']))
        return redirect('/webpage_link')
      elif 'update' in request.form:
        data = databaseHandler.get_single(
            ST.query_list['website_link_page']['get_single_record'].format(
                id=request.form['update']))
        return render_template('add_new_site_form.html', existing_data=data)
      else:
        databaseHandler.update_value(
            ST.query_list['website_link_page']['update_query'].format(
                title=request.form['site_title'],
                link=request.form['site_link'],
                desc=request.form['site_desc'],
                id=request.form['update_id']))

    website_user_data = databaseHandler.get_data(
        ST.query_list['common_query']['special_select'].format(
            tablename='website_links_table', user=session['username']))
    return render_template('webpage_link_page.html',
                           saved_site_data=website_user_data)
  return redirect('/login')


@app.route('/add_webpage_link', methods=['GET', 'POST'])
def add_webpage_link_page():
  if 'username' in session:
    if request.method == 'POST':
      datalist = [
          request.form['site_title'], request.form['site_link'],
          request.form['site_desc']
      ]
      databaseHandler.Insert_data(
          ST.query_list['website_link_page']['insert_query'].format(
              title=datalist[0],
              link=datalist[1],
              desc=datalist[2],
              user=session['username']))
      return redirect('/webpage_link')
    data = [['', '', '', '']]
    return render_template('add_new_site_form.html', existing_data=data)
  return redirect('login')


@app.route('/data', methods=['GET', 'POST'])
def data():
  return render_template('session_test.html', data=dict(session))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
