import {render, screen, cleanup} from '@testing-library/react';
import renderer from 'react-test-renderer';
import Todo from './Todo';

afterEach(() => {
  cleanup();
});

test('toBeTrue', () => {
  expect(true).toBe(true);
})

test('should render non-completed todo', () => {

  const item = {id: 1, title: 'wash dishes', completed: false};

  render(<Todo item={item}/>);
  const todoElement = screen.getByTestId('todo-1');
  expect(todoElement).toBeInTheDocument();
  expect(todoElement).toHaveTextContent('wash dishes');
  expect(todoElement).toContainHTML('div');
  expect(todoElement).not.toContainHTML('strike');
})

test('should render completed todo', () => {

  const item = {id: 2, title: 'do laundry', completed: true};

  render(<Todo item={item}/>);
  const todoElement = screen.getByTestId('todo-2');
  expect(todoElement).toBeInTheDocument();
  expect(todoElement).toHaveTextContent('do laundry');
  expect(todoElement).toContainHTML('strike');
})


test('matches snapshot', () => {

  const item = {id: 1, title: 'wash dishes', completed: true};

  const tree = renderer.create(<Todo item={item}/>).toJSON();
  // when console.log(tree):
  // tree = 
  // {
  //   type: 'div',
  //   props: { 'data-testid': 'todo-1' },
  //   children: [ { type: 'strike', props: {}, children: [Array] } ]
  // }

  expect(tree).toMatchSnapshot();
})