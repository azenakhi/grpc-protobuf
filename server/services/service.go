package services

import (
	context "context"
)

type TaskService struct{}

func (t TaskService) List(context.Context, *Void) (*TaskList, error) {
	task1 := &Task{Text: "Task 1", Done: true}
	task2 := &Task{Text: "Task 2", Done: true}
	task3 := &Task{Text: "Task 3", Done: true}
	tasks := &TaskList{}
	tasks.Tasks = append(tasks.Tasks, task1)
	tasks.Tasks = append(tasks.Tasks, task2)
	tasks.Tasks = append(tasks.Tasks, task3)
	return tasks, nil

}
func (t TaskService) Add(context.Context, *Task) (*Task, error) {
	return nil, nil
}
