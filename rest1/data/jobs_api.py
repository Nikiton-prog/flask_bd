import flask
from flask import jsonify, make_response, request

from . import db_session
from .users import User
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'team_leader'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Job).get(jobs_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'job': job.to_dict(only=('job', 'work_size', 'team_leader'))
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Job(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})