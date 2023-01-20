const Todo = ({item}) => {

  const {id, title, completed} = item;
  
  const h1 = <h1>{title}</h1>;
  const text = completed? <strike>{h1}</strike> : h1;

  return (
    <div data-testid={`todo-${id}`}>{text}</div>
  )
}
export default Todo;