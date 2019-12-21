# System Solver API
by Ganesh Sankaran
<hr />
<h3>Overview</h3>
<p>This 
<a href="https://system-solver-api.herokuapp.com">Flask API</a>
provides an endpoint to solve systems of linear equations with two variables using the 
<a href="https://github.com/Z3Prover/z3">Z3 SMT solver</a>.</p>

<p>An example of such a system is 
<code>{3x + 2y = 6, x - 4y = 5}</code>, whose unique solution is <code>(x, y) = (17/7, -9/14)</code>.</p>

<p>In general, these systems are of the form
<code>{a_1_1 * x + a_1_2 * y = b_1, a_2_1 * x + a_2_2 * y = b_2}</code> and can be</p>
<ul>
  <li>inconsistent systems (no solution)</li>
  <li>independent systems (unique solution)</li>
  <li>dependent systems (infinitely many solutions)</li>
</ul>

<p>This API identifies the type of system and provides a solution if the system is independent.</p>
<hr />
<h3>API Endpoints</h3>
<pre><strong>GET /api/v1/solve</strong></pre>

<p>Request Parameters</p>
<ul>
  <li><code>a_1_1</code>: a floating point number</li>
  <li><code>a_1_2</code>: a floating point number</li>
  <li><code>a_2_1</code>: a floating point number</li>
  <li><code>a_2_2</code>: a floating point number</li>
  <li><code>b_1</code>: a floating point number</li>
  <li><code>b_2</code>: a floating point number</li>
</ul>

<p>Response Parameters</p>
<ul>
  <li><code>x</code>: <code>null</code> or a string representing the x-value</li>
  <li><code>y</code>: <code>null</code> or a string representing the y-value</li>
  <li><code>notes</code>: a string identifying the type of system</li>
</ul>
