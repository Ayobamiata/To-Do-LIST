
from flask import Flask,request,Blueprint
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)


tasks=[]

class TaskListResource(Resource):
    def get(self):
        return tasks

    def post(self):
        data=request.get_json()
        task={
            "id":len(tasks)+1,
            "title":data['title'],
            "done":False
        }

        tasks.append(task)
        return task,201


class TaskResource(Resource):
    def get(self,task_id):
        for task in tasks:
            if task['id']==task_id:
                return task

        return {"error":"Task not found"},404


    def put(self,task_id):
        data=request.get_json()

        for task in tasks:
            if task['id']==task_id:
                task['title']=data.get('title',task['title'])
                task['done']=data.get('done',task['title'])

                return task

        return {'error':"Task not found"},404


# @app.route('/task/<int:task_id>',methods=['DELETE'])
# def delete(task_id):
#     global tasks
#     tasks=[t for t in tasks if t['id]' != task_id]]
#     return jsonify({"message":"Deleted"})

    def delete(self,task_id):
        global tasks

        for task in tasks:
            if task['id'] == task_id:
                tasks = [t for t in tasks if t['id'] != task_id]
                return {"message": "Deleted"}, 200

        return {"error": "Task not found"}, 404


api.add_resource(TaskListResource,"/task")
api.add_resource(TaskResource,"/task/<int:task_id>")






if __name__== '__main__':
    app.run(debug=True)

