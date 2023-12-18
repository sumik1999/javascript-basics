const { connect } = require("./connectDb.js");
const Todo = require("./TodoModel.js");

const createTodo = async () => {
  try {
    await connect();
    const todo = await Todo.addTask({
      title: "New todo",
      dueDate: new Date(),
      completed: true,
    });
    console.log(`todo created with id : `, { todo });
  } catch (error) {
    console.error(error);
  }
};

const countItems = async () => {
  try {
    const count = await Todo.count();
    console.log(`Found ${count} items`);
  } catch (error) {
    console.error(error);
  }
};

const listItems = async () => {
  try {
    const todos = await Todo.findAll({
      order: [["id", "ASC"]],
    }); //await before every db function
    const todoList = todos.map((todo) => todo.displayableString()).join("\n");
    console.log(todoList);
  } catch (error) {
    console.error(error);
  }
};

const getItem = async (reqid) => {
  try {
    const todo = await Todo.findOne({
      where: {
        id: reqid,
      },
    });
    console.log(todo.displayableString());
  } catch {}
};

(async () => {
  await countItems();
  await listItems();
  await getItem(1);
})();
