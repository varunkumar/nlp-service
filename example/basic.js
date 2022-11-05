// fetch multipart/form-data
const formData = new FormData();
formData.append(
  'question',
  `
Instructions: Given an input question, respond with syntactically correct PostgreSQL. Be creative but the SQL must be correct. Only use tables called "users" and "charges". The "users" table has columns: id (integer), signup_dt (timestamp), email (character varying), and plan_type (character varying). The "charges" table has columns: amount (bigint), user_id (integer), and charge_dt (timestamp).

how much revenue did we have in the past 7 days?
`
);

const testPost = () => {
  fetch('http://localhost:7000/api/askdata', {
    method: 'POST',
    body: formData,
  })
    .then((res) => res.text())
    .then((res) => console.log(res))
    .catch((err) => console.log(err));
};

testPost();
