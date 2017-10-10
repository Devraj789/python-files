Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">


<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    
    <title>3. An Informal Introduction to Python &mdash; Python 3.4.7 documentation</title>
    
    <link rel="stylesheet" href="../_static/pydoctheme.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
    
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    '../',
        VERSION:     '3.4.7',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true
      };
    </script>
    <script type="text/javascript" src="../_static/jquery.js"></script>
    <script type="text/javascript" src="../_static/underscore.js"></script>
    <script type="text/javascript" src="../_static/doctools.js"></script>
    <script type="text/javascript" src="../_static/sidebar.js"></script>
    <link rel="search" type="application/opensearchdescription+xml"
          title="Search within Python 3.4.7 documentation"
          href="../_static/opensearch.xml"/>
    <link rel="author" title="About these documents" href="../about.html" />
    <link rel="copyright" title="Copyright" href="../copyright.html" />
    <link rel="top" title="Python 3.4.7 documentation" href="../contents.html" />
    <link rel="up" title="The Python Tutorial" href="index.html" />
    <link rel="next" title="4. More Control Flow Tools" href="controlflow.html" />
    <link rel="prev" title="2. Using the Python Interpreter" href="interpreter.html" />
    <link rel="shortcut icon" type="image/png" href="../_static/py.png" />
    <script type="text/javascript" src="../_static/copybutton.js"></script>
    
    
 

  </head>
  <body role="document">  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="controlflow.html" title="4. More Control Flow Tools"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="interpreter.html" title="2. Using the Python Interpreter"
             accesskey="P">previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <a href="../index.html">3.4.7 Documentation</a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" accesskey="U">The Python Tutorial</a> &raquo;</li> 
      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <div class="section" id="an-informal-introduction-to-python">
<span id="tut-informal"></span><h1>3. An Informal Introduction to Python<a class="headerlink" href="#an-informal-introduction-to-python" title="Permalink to this headline">¶</a></h1>
<p>In the following examples, input and output are distinguished by the presence or
absence of prompts (<a class="reference internal" href="../glossary.html#term"><span class="xref std std-term">&gt;&gt;&gt;</span></a> and <a class="reference internal" href="../glossary.html#term-1"><span class="xref std std-term">...</span></a>): to repeat the example, you must type
everything after the prompt, when the prompt appears; lines that do not begin
with a prompt are output from the interpreter. Note that a secondary prompt on a
line by itself in an example means you must type a blank line; this is used to
end a multi-line command.</p>
<p>Many of the examples in this manual, even those entered at the interactive
prompt, include comments.  Comments in Python start with the hash character,
<code class="docutils literal"><span class="pre">#</span></code>, and extend to the end of the physical line.  A comment may appear at the
start of a line or following whitespace or code, but not within a string
literal.  A hash character within a string literal is just a hash character.
Since comments are to clarify code and are not interpreted by Python, they may
be omitted when typing in examples.</p>
<p>Some examples:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="c1"># this is the first comment</span>
<span class="n">spam</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># and this is the second comment</span>
          <span class="c1"># ... and now a third!</span>
<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;# This is not a comment because it&#39;s inside quotes.&quot;</span>
</pre></div>
</div>
<div class="section" id="using-python-as-a-calculator">
<span id="tut-calculator"></span><h2>3.1. Using Python as a Calculator<a class="headerlink" href="#using-python-as-a-calculator" title="Permalink to this headline">¶</a></h2>
<p>Let&#8217;s try some simple Python commands.  Start the interpreter and wait for the
primary prompt, <code class="docutils literal"><span class="pre">&gt;&gt;&gt;</span></code>.  (It shouldn&#8217;t take long.)</p>
<div class="section" id="numbers">
<span id="tut-numbers"></span><h3>3.1.1. Numbers<a class="headerlink" href="#numbers" title="Permalink to this headline">¶</a></h3>
<p>The interpreter acts as a simple calculator: you can type an expression at it
and it will write the value.  Expression syntax is straightforward: the
operators <code class="docutils literal"><span class="pre">+</span></code>, <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">*</span></code> and <code class="docutils literal"><span class="pre">/</span></code> work just like in most other languages
(for example, Pascal or C); parentheses (<code class="docutils literal"><span class="pre">()</span></code>) can be used for grouping.
For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">+</span> <span class="mi">2</span>
<span class="go">4</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span>
<span class="go">20</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span>
<span class="go">5.0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">8</span> <span class="o">/</span> <span class="mi">5</span>  <span class="c1"># division always returns a floating point number</span>
<span class="go">1.6</span>
</pre></div>
</div>
<p>The integer numbers (e.g. <code class="docutils literal"><span class="pre">2</span></code>, <code class="docutils literal"><span class="pre">4</span></code>, <code class="docutils literal"><span class="pre">20</span></code>) have type <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a>,
the ones with a fractional part (e.g. <code class="docutils literal"><span class="pre">5.0</span></code>, <code class="docutils literal"><span class="pre">1.6</span></code>) have type
<a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>.  We will see more about numeric types later in the tutorial.</p>
<p>Division (<code class="docutils literal"><span class="pre">/</span></code>) always returns a float.  To do <a class="reference internal" href="../glossary.html#term-floor-division"><span class="xref std std-term">floor division</span></a> and
get an integer result (discarding any fractional result) you can use the <code class="docutils literal"><span class="pre">//</span></code>
operator; to calculate the remainder you can use <code class="docutils literal"><span class="pre">%</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">/</span> <span class="mi">3</span>  <span class="c1"># classic division returns a float</span>
<span class="go">5.666666666666667</span>
<span class="go">&gt;&gt;&gt;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">//</span> <span class="mi">3</span>  <span class="c1"># floor division discards the fractional part</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">%</span> <span class="mi">3</span>  <span class="c1"># the % operator returns the remainder of the division</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">+</span> <span class="mi">2</span>  <span class="c1"># result * divisor + remainder</span>
<span class="go">17</span>
</pre></div>
</div>
<p>With Python, it is possible to use the <code class="docutils literal"><span class="pre">**</span></code> operator to calculate powers <a class="footnote-reference" href="#id3" id="id1">[1]</a>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">**</span> <span class="mi">2</span>  <span class="c1"># 5 squared</span>
<span class="go">25</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">**</span> <span class="mi">7</span>  <span class="c1"># 2 to the power of 7</span>
<span class="go">128</span>
</pre></div>
</div>
<p>The equal sign (<code class="docutils literal"><span class="pre">=</span></code>) is used to assign a value to a variable. Afterwards, no
result is displayed before the next interactive prompt:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">=</span> <span class="mi">20</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">height</span> <span class="o">=</span> <span class="mi">5</span> <span class="o">*</span> <span class="mi">9</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">*</span> <span class="n">height</span>
<span class="go">900</span>
</pre></div>
</div>
<p>If a variable is not &#8220;defined&#8221; (assigned a value), trying to use it will
give you an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">n</span>  <span class="c1"># try to access an undefined variable</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">NameError</span>: <span class="n">name &#39;n&#39; is not defined</span>
</pre></div>
</div>
<p>There is full support for floating point; operators with mixed type operands
convert the integer operand to floating point:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="mf">3.75</span> <span class="o">/</span> <span class="mf">1.5</span>
<span class="go">7.5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mf">7.0</span> <span class="o">/</span> <span class="mi">2</span>
<span class="go">3.5</span>
</pre></div>
</div>
<p>In interactive mode, the last printed expression is assigned to the variable
<code class="docutils literal"><span class="pre">_</span></code>.  This means that when you are using Python as a desk calculator, it is
somewhat easier to continue calculations, for example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">tax</span> <span class="o">=</span> <span class="mf">12.5</span> <span class="o">/</span> <span class="mi">100</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">=</span> <span class="mf">100.50</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">*</span> <span class="n">tax</span>
<span class="go">12.5625</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">+</span> <span class="n">_</span>
<span class="go">113.0625</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="go">113.06</span>
</pre></div>
</div>
<p>This variable should be treated as read-only by the user.  Don&#8217;t explicitly
assign a value to it &#8212; you would create an independent local variable with the
same name masking the built-in variable with its magic behavior.</p>
<p>In addition to <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> and <a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, Python supports other types of
numbers, such as <a class="reference internal" href="../library/decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal"><span class="pre">Decimal</span></code></a> and <a class="reference internal" href="../library/fractions.html#fractions.Fraction" title="fractions.Fraction"><code class="xref py py-class docutils literal"><span class="pre">Fraction</span></code></a>.
Python also has built-in support for <a class="reference internal" href="../library/stdtypes.html#typesnumeric"><span class="std std-ref">complex numbers</span></a>,
and uses the <code class="docutils literal"><span class="pre">j</span></code> or <code class="docutils literal"><span class="pre">J</span></code> suffix to indicate the imaginary part
(e.g. <code class="docutils literal"><span class="pre">3+5j</span></code>).</p>
</div>
<div class="section" id="strings">
<span id="tut-strings"></span><h3>3.1.2. Strings<a class="headerlink" href="#strings" title="Permalink to this headline">¶</a></h3>
<p>Besides numbers, Python can also manipulate strings, which can be expressed
in several ways.  They can be enclosed in single quotes (<code class="docutils literal"><span class="pre">'...'</span></code>) or
double quotes (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) with the same result <a class="footnote-reference" href="#id4" id="id2">[2]</a>.  <code class="docutils literal"><span class="pre">\</span></code> can be used
to escape quotes:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;spam eggs&#39;</span>  <span class="c1"># single quotes</span>
<span class="go">&#39;spam eggs&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;doesn</span><span class="se">\&#39;</span><span class="s1">t&#39;</span>  <span class="c1"># use \&#39; to escape the single quote...</span>
<span class="go">&quot;doesn&#39;t&quot;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;doesn&#39;t&quot;</span>  <span class="c1"># ...or use double quotes instead</span>
<span class="go">&quot;doesn&#39;t&quot;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;</span><span class="se">\&quot;</span><span class="s2">Yes,</span><span class="se">\&quot;</span><span class="s2"> he said.&quot;</span>
<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>
<span class="go">&#39;&quot;Isn\&#39;t,&quot; she said.&#39;</span>
</pre></div>
</div>
<p>In the interactive interpreter, the output string is enclosed in quotes and
special characters are escaped with backslashes.  While this might sometimes
look different from the input (the enclosing quotes could change), the two
strings are equivalent.  The string is enclosed in double quotes if
the string contains a single quote and no double quotes, otherwise it is
enclosed in single quotes.  The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function produces a more
readable output, by omitting the enclosing quotes and by printing escaped
and special characters:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>
<span class="go">&#39;&quot;Isn\&#39;t,&quot; she said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span><span class="p">)</span>
<span class="go">&quot;Isn&#39;t,&quot; she said.</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;First line.</span><span class="se">\n</span><span class="s1">Second line.&#39;</span>  <span class="c1"># \n means newline</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span>  <span class="c1"># without print(), \n is included in the output</span>
<span class="go">&#39;First line.\nSecond line.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>  <span class="c1"># with print(), \n produces a new line</span>
<span class="go">First line.</span>
<span class="go">Second line.</span>
</pre></div>
</div>
<p>If you don&#8217;t want characters prefaced by <code class="docutils literal"><span class="pre">\</span></code> to be interpreted as
special characters, you can use <em>raw strings</em> by adding an <code class="docutils literal"><span class="pre">r</span></code> before
the first quote:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;C:\some</span><span class="se">\n</span><span class="s1">ame&#39;</span><span class="p">)</span>  <span class="c1"># here \n means newline!</span>
<span class="go">C:\some</span>
<span class="go">ame</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;C:\some\name&#39;</span><span class="p">)</span>  <span class="c1"># note the r before the quote</span>
<span class="go">C:\some\name</span>
</pre></div>
</div>
<p>String literals can span multiple lines.  One way is using triple-quotes:
<code class="docutils literal"><span class="pre">&quot;&quot;&quot;...&quot;&quot;&quot;</span></code> or <code class="docutils literal"><span class="pre">'''...'''</span></code>.  End of lines are automatically
included in the string, but it&#8217;s possible to prevent this by adding a <code class="docutils literal"><span class="pre">\</span></code> at
the end of the line.  The following example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">Usage: thingy [OPTIONS]</span>
<span class="s2">     -h                        Display this usage message</span>
<span class="s2">     -H hostname               Hostname to connect to</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>produces the following output (note that the initial newline is not included):</p>
<div class="highlight-text"><div class="highlight"><pre><span></span>Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
</pre></div>
</div>
<p>Strings can be concatenated (glued together) with the <code class="docutils literal"><span class="pre">+</span></code> operator, and
repeated with <code class="docutils literal"><span class="pre">*</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># 3 times &#39;un&#39;, followed by &#39;ium&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="s1">&#39;un&#39;</span> <span class="o">+</span> <span class="s1">&#39;ium&#39;</span>
<span class="go">&#39;unununium&#39;</span>
</pre></div>
</div>
<p>Two or more <em>string literals</em> (i.e. the ones enclosed between quotes) next
to each other are automatically concatenated.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Py&#39;</span> <span class="s1">&#39;thon&#39;</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>This only works with two literals though, not with variables or expressions:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">=</span> <span class="s1">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="s1">&#39;thon&#39;</span>  <span class="c1"># can&#39;t concatenate a variable and a string literal</span>
<span class="go">  ...</span>
<span class="go">SyntaxError: invalid syntax</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="s1">&#39;un&#39;</span> <span class="o">*</span> <span class="mi">3</span><span class="p">)</span> <span class="s1">&#39;ium&#39;</span>
<span class="go">  ...</span>
<span class="go">SyntaxError: invalid syntax</span>
</pre></div>
</div>
<p>If you want to concatenate variables or a variable and a literal, use <code class="docutils literal"><span class="pre">+</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">+</span> <span class="s1">&#39;thon&#39;</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>This feature is particularly useful when you want to break long strings:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">text</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Put several strings within parentheses &#39;</span>
<span class="go">            &#39;to have them joined together.&#39;)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">text</span>
<span class="go">&#39;Put several strings within parentheses to have them joined together.&#39;</span>
</pre></div>
</div>
<p>Strings can be <em>indexed</em> (subscripted), with the first character having index 0.
There is no separate character type; a character is simply a string of size
one:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span> <span class="o">=</span> <span class="s1">&#39;Python&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># character in position 0</span>
<span class="go">&#39;P&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># character in position 5</span>
<span class="go">&#39;n&#39;</span>
</pre></div>
</div>
<p>Indices may also be negative numbers, to start counting from the right:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>  <span class="c1"># last character</span>
<span class="go">&#39;n&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># second-last character</span>
<span class="go">&#39;o&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">6</span><span class="p">]</span>
<span class="go">&#39;P&#39;</span>
</pre></div>
</div>
<p>Note that since -0 is the same as 0, negative indices start from -1.</p>
<p>In addition to indexing, <em>slicing</em> is also supported.  While indexing is used
to obtain individual characters, <em>slicing</em> allows you to obtain substring:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># characters from position 0 (included) to 2 (excluded)</span>
<span class="go">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># characters from position 2 (included) to 5 (excluded)</span>
<span class="go">&#39;tho&#39;</span>
</pre></div>
</div>
<p>Note how the start is always included, and the end always excluded.  This
makes sure that <code class="docutils literal"><span class="pre">s[:i]</span> <span class="pre">+</span> <span class="pre">s[i:]</span></code> is always equal to <code class="docutils literal"><span class="pre">s</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span>
<span class="go">&#39;Python&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>Slice indices have useful defaults; an omitted first index defaults to zero, an
omitted second index defaults to the size of the string being sliced.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># character from the beginning to position 2 (excluded)</span>
<span class="go">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>  <span class="c1"># characters from position 4 (included) to the end</span>
<span class="go">&#39;on&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="c1"># characters from the second-last (included) to the end</span>
<span class="go">&#39;on&#39;</span>
</pre></div>
</div>
<p>One way to remember how slices work is to think of the indices as pointing
<em>between</em> characters, with the left edge of the first character numbered 0.
Then the right edge of the last character of a string of <em>n</em> characters has
index <em>n</em>, for example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span> <span class="o">+---+---+---+---+---+---+</span>
 <span class="o">|</span> <span class="n">P</span> <span class="o">|</span> <span class="n">y</span> <span class="o">|</span> <span class="n">t</span> <span class="o">|</span> <span class="n">h</span> <span class="o">|</span> <span class="n">o</span> <span class="o">|</span> <span class="n">n</span> <span class="o">|</span>
 <span class="o">+---+---+---+---+---+---+</span>
 <span class="mi">0</span>   <span class="mi">1</span>   <span class="mi">2</span>   <span class="mi">3</span>   <span class="mi">4</span>   <span class="mi">5</span>   <span class="mi">6</span>
<span class="o">-</span><span class="mi">6</span>  <span class="o">-</span><span class="mi">5</span>  <span class="o">-</span><span class="mi">4</span>  <span class="o">-</span><span class="mi">3</span>  <span class="o">-</span><span class="mi">2</span>  <span class="o">-</span><span class="mi">1</span>
</pre></div>
</div>
<p>The first row of numbers gives the position of the indices 0...6 in the string;
the second row gives the corresponding negative indices. The slice from <em>i</em> to
<em>j</em> consists of all characters between the edges labeled <em>i</em> and <em>j</em>,
respectively.</p>
<p>For non-negative indices, the length of a slice is the difference of the
indices, if both are within bounds.  For example, the length of <code class="docutils literal"><span class="pre">word[1:3]</span></code> is
2.</p>
<p>Attempting to use an index that is too large will result in an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">]</span>  <span class="c1"># the word only has 6 characters</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">IndexError</span>: <span class="n">string index out of range</span>
</pre></div>
</div>
<p>However, out of range slice indexes are handled gracefully when used for
slicing:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="mi">42</span><span class="p">]</span>
<span class="go">&#39;on&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">:]</span>
<span class="go">&#39;&#39;</span>
</pre></div>
</div>
<p>Python strings cannot be changed &#8212; they are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>.
Therefore, assigning to an indexed position in the string results in an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;J&#39;</span>
<span class="go">  ...</span>
<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span> <span class="o">=</span> <span class="s1">&#39;py&#39;</span>
<span class="go">  ...</span>
<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>
</pre></div>
</div>
<p>If you need a different string, you should create a new one:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;J&#39;</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<span class="go">&#39;Jython&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="s1">&#39;py&#39;</span>
<span class="go">&#39;Pypy&#39;</span>
</pre></div>
</div>
<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> returns the length of a string:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;supercalifragilisticexpialidocious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<span class="go">34</span>
</pre></div>
</div>
<div class="admonition seealso">
<p class="first admonition-title">See also</p>
<dl class="last docutils">
<dt><a class="reference internal" href="../library/stdtypes.html#textseq"><span class="std std-ref">Text Sequence Type &#8212; str</span></a></dt>
<dd>Strings are examples of <em>sequence types</em>, and support the common
operations supported by such types.</dd>
<dt><a class="reference internal" href="../library/stdtypes.html#string-methods"><span class="std std-ref">String Methods</span></a></dt>
<dd>Strings support a large number of methods for
basic transformations and searching.</dd>
<dt><a class="reference internal" href="../library/string.html#string-formatting"><span class="std std-ref">String Formatting</span></a></dt>
<dd>Information about string formatting with <a class="reference internal" href="../library/stdtypes.html#str.format" title="str.format"><code class="xref py py-meth docutils literal"><span class="pre">str.format()</span></code></a> is described
here.</dd>
<dt><a class="reference internal" href="../library/stdtypes.html#old-string-formatting"><span class="std std-ref">printf-style String Formatting</span></a></dt>
<dd>The old formatting operations invoked when strings and Unicode strings are
the left operand of the <code class="docutils literal"><span class="pre">%</span></code> operator are described in more detail here.</dd>
</dl>
</div>
</div>
<div class="section" id="lists">
<span id="tut-lists"></span><h3>3.1.3. Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h3>
<p>Python knows a number of <em>compound</em> data types, used to group together other
values.  The most versatile is the <em>list</em>, which can be written as a list of
comma-separated values (items) between square brackets.  Lists might contain
items of different types, but usually the items all have the same type.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">25</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span>
<span class="go">[1, 4, 9, 16, 25]</span>
</pre></div>
</div>
<p>Like strings (and all other built-in <a class="reference internal" href="../glossary.html#term-sequence"><span class="xref std std-term">sequence</span></a> type), lists can be
indexed and sliced:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># indexing returns the item</span>
<span class="go">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">25</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span>  <span class="c1"># slicing returns a new list</span>
<span class="go">[9, 16, 25]</span>
</pre></div>
</div>
<p>All slice operations return a new list containing the requested elements.  This
means that the following slice returns a new (shallow) copy of the list:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[:]</span>
<span class="go">[1, 4, 9, 16, 25]</span>
</pre></div>
</div>
<p>Lists also support operations like concatenation:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">+</span> <span class="p">[</span><span class="mi">36</span><span class="p">,</span> <span class="mi">49</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="mi">81</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>
<span class="go">[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]</span>
</pre></div>
</div>
<p>Unlike strings, which are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>, lists are a <a class="reference internal" href="../glossary.html#term-mutable"><span class="xref std std-term">mutable</span></a>
type, i.e. it is possible to change their content:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span> <span class="mi">125</span><span class="p">]</span>  <span class="c1"># something&#39;s wrong here</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">4</span> <span class="o">**</span> <span class="mi">3</span>  <span class="c1"># the cube of 4 is 64, not 65!</span>
<span class="go">64</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mi">64</span>  <span class="c1"># replace the wrong value</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>
<span class="go">[1, 8, 27, 64, 125]</span>
</pre></div>
</div>
<p>You can also add new items at the end of the list, by using
the <code class="xref py py-meth docutils literal"><span class="pre">append()</span></code> <em>method</em> (we will see more about methods later):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">216</span><span class="p">)</span>  <span class="c1"># add the cube of 6</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">7</span> <span class="o">**</span> <span class="mi">3</span><span class="p">)</span>  <span class="c1"># and the cube of 7</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>
<span class="go">[1, 8, 27, 64, 125, 216, 343]</span>
</pre></div>
</div>
<p>Assignment to slices is also possible, and this can even change the size of the
list or clear it entirely:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="s1">&#39;e&#39;</span><span class="p">,</span> <span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># replace some values</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;C&#39;</span><span class="p">,</span> <span class="s1">&#39;D&#39;</span><span class="p">,</span> <span class="s1">&#39;E&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># now remove them</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># clear the list by replacing all the elements with an empty list</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[:]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[]</span>
</pre></div>
</div>
<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> also applies to lists:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">letters</span><span class="p">)</span>
<span class="go">4</span>
</pre></div>
</div>
<p>It is possible to nest lists (create lists containing other lists), for
example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">n</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span><span class="p">,</span> <span class="n">n</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span>
<span class="go">[[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;], [1, 2, 3]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
<span class="go">&#39;b&#39;</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="first-steps-towards-programming">
<span id="tut-firststeps"></span><h2>3.2. First Steps Towards Programming<a class="headerlink" href="#first-steps-towards-programming" title="Permalink to this headline">¶</a></h2>
<p>Of course, we can use Python for more complicated tasks than adding two and two
together.  For instance, we can write an initial sub-sequence of the <em>Fibonacci</em>
series as follows:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># Fibonacci series:</span>
<span class="gp">... </span><span class="c1"># the sum of two elements defines the next</span>
<span class="gp">... </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
<span class="gp">...</span>
<span class="go">1</span>
<span class="go">1</span>
<span class="go">2</span>
<span class="go">3</span>
<span class="go">5</span>
<span class="go">8</span>
</pre></div>
</div>
<p>This example introduces several new features.</p>
<ul>
<li><p class="first">The first line contains a <em>multiple assignment</em>: the variables <code class="docutils literal"><span class="pre">a</span></code> and <code class="docutils literal"><span class="pre">b</span></code>
simultaneously get the new values 0 and 1.  On the last line this is used again,
demonstrating that the expressions on the right-hand side are all evaluated
first before any of the assignments take place.  The right-hand side expressions
are evaluated  from the left to the right.</p>
</li>
<li><p class="first">The <a class="reference internal" href="../reference/compound_stmts.html#while"><code class="xref std std-keyword docutils literal"><span class="pre">while</span></code></a> loop executes as long as the condition (here: <code class="docutils literal"><span class="pre">b</span> <span class="pre">&lt;</span> <span class="pre">10</span></code>)
remains true.  In Python, like in C, any non-zero integer value is true; zero is
false.  The condition may also be a string or list value, in fact any sequence;
anything with a non-zero length is true, empty sequences are false.  The test
used in the example is a simple comparison.  The standard comparison operators
are written the same as in C: <code class="docutils literal"><span class="pre">&lt;</span></code> (less than), <code class="docutils literal"><span class="pre">&gt;</span></code> (greater than), <code class="docutils literal"><span class="pre">==</span></code>
(equal to), <code class="docutils literal"><span class="pre">&lt;=</span></code> (less than or equal to), <code class="docutils literal"><span class="pre">&gt;=</span></code> (greater than or equal to)
and <code class="docutils literal"><span class="pre">!=</span></code> (not equal to).</p>
</li>
<li><p class="first">The <em>body</em> of the loop is <em>indented</em>: indentation is Python&#8217;s way of grouping
statements.  At the interactive prompt, you have to type a tab or space(s) for
each indented line.  In practice you will prepare more complicated input
for Python with a text editor; all decent text editors have an auto-indent
facility.  When a compound statement is entered interactively, it must be
followed by a blank line to indicate completion (since the parser cannot
guess when you have typed the last line).  Note that each line within a basic
block must be indented by the same amount.</p>
</li>
<li><p class="first">The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function writes the value of the argument(s) it is given.
It differs from just writing the expression you want to write (as we did
earlier in the calculator examples) in the way it handles multiple arguments,
floating point quantities, and strings.  Strings are printed without quotes,
and a space is inserted between items, so you can format things nicely, like
this:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">i</span> <span class="o">=</span> <span class="mi">256</span><span class="o">*</span><span class="mi">256</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;The value of i is&#39;</span><span class="p">,</span> <span class="n">i</span><span class="p">)</span>
<span class="go">The value of i is 65536</span>
</pre></div>
</div>
<p>The keyword argument <em>end</em> can be used to avoid the newline after the output,
or end the output with a different string:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">1000</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
<span class="gp">...</span>
<span class="go">1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,</span>
</pre></div>
</div>
</li>
</ul>
<p class="rubric">Footnotes</p>
<table class="docutils footnote" frame="void" id="id3" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>Since <code class="docutils literal"><span class="pre">**</span></code> has higher precedence than <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">-3**2</span></code> will be
interpreted as <code class="docutils literal"><span class="pre">-(3**2)</span></code> and thus result in <code class="docutils literal"><span class="pre">-9</span></code>.  To avoid this
and get <code class="docutils literal"><span class="pre">9</span></code>, you can use <code class="docutils literal"><span class="pre">(-3)**2</span></code>.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id4" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>Unlike other languages, special characters such as <code class="docutils literal"><span class="pre">\n</span></code> have the
same meaning with both single (<code class="docutils literal"><span class="pre">'...'</span></code>) and double (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) quotes.
The only difference between the two is that within single quotes you don&#8217;t
need to escape <code class="docutils literal"><span class="pre">&quot;</span></code> (but you have to escape <code class="docutils literal"><span class="pre">\'</span></code>) and vice versa.</td></tr>
</tbody>
</table>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h3><a href="../contents.html">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#">3. An Informal Introduction to Python</a><ul>
<li><a class="reference internal" href="#using-python-as-a-calculator">3.1. Using Python as a Calculator</a><ul>
<li><a class="reference internal" href="#numbers">3.1.1. Numbers</a></li>
<li><a class="reference internal" href="#strings">3.1.2. Strings</a></li>
<li><a class="reference internal" href="#lists">3.1.3. Lists</a></li>
</ul>
</li>
<li><a class="reference internal" href="#first-steps-towards-programming">3.2. First Steps Towards Programming</a></li>
</ul>
</li>
</ul>

  <h4>Previous topic</h4>
  <p class="topless"><a href="interpreter.html"
                        title="previous chapter">2. Using the Python Interpreter</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="controlflow.html"
                        title="next chapter">4. More Control Flow Tools</a></p>
<h3>This Page</h3>
<ul class="this-page-menu">
  <li><a href="../bugs.html">Report a Bug</a></li>
  <li><a href="../_sources/tutorial/introduction.txt"
         rel="nofollow">Show Source</a></li>
</ul>

<div id="searchbox" style="display: none" role="search">
  <h3>Quick search</h3>
    <form class="search" action="../search.html" method="get">
      <div><input type="text" name="q" /></div>
      <div><input type="submit" value="Go" /></div>
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="controlflow.html" title="4. More Control Flow Tools"
             >next</a> |</li>
        <li class="right" >
          <a href="interpreter.html" title="2. Using the Python Interpreter"
             >previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <a href="../index.html">3.4.7 Documentation</a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" >The Python Tutorial</a> &raquo;</li> 
      </ul>
    </div>  
    <div class="footer">
    &copy; <a href="../copyright.html">Copyright</a> 1990-2017, Python Software Foundation.
    <br />
    The Python Software Foundation is a non-profit corporation.
    <a href="https://www.python.org/psf/donations/">Please donate.</a>
    <br />
    Last updated on Aug 09, 2017.
    <a href="../bugs.html">Found a bug</a>?
    <br />
    Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.4.4.
    </div>

  </body>
  
</html>"""
>>> html
'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n    \n    <title>3. An Informal Introduction to Python &mdash; Python 3.4.7 documentation</title>\n    \n    <link rel="stylesheet" href="../_static/pydoctheme.css" type="text/css" />\n    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />\n    \n    <script type="text/javascript">\n      var DOCUMENTATION_OPTIONS = {\n        URL_ROOT:    \'../\',\n        VERSION:     \'3.4.7\',\n        COLLAPSE_INDEX: false,\n        FILE_SUFFIX: \'.html\',\n        HAS_SOURCE:  true\n      };\n    </script>\n    <script type="text/javascript" src="../_static/jquery.js"></script>\n    <script type="text/javascript" src="../_static/underscore.js"></script>\n    <script type="text/javascript" src="../_static/doctools.js"></script>\n    <script type="text/javascript" src="../_static/sidebar.js"></script>\n    <link rel="search" type="application/opensearchdescription+xml"\n          title="Search within Python 3.4.7 documentation"\n          href="../_static/opensearch.xml"/>\n    <link rel="author" title="About these documents" href="../about.html" />\n    <link rel="copyright" title="Copyright" href="../copyright.html" />\n    <link rel="top" title="Python 3.4.7 documentation" href="../contents.html" />\n    <link rel="up" title="The Python Tutorial" href="index.html" />\n    <link rel="next" title="4. More Control Flow Tools" href="controlflow.html" />\n    <link rel="prev" title="2. Using the Python Interpreter" href="interpreter.html" />\n    <link rel="shortcut icon" type="image/png" href="../_static/py.png" />\n    <script type="text/javascript" src="../_static/copybutton.js"></script>\n    \n    \n \n\n  </head>\n  <body role="document">  \n    <div class="related" role="navigation" aria-label="related navigation">\n      <h3>Navigation</h3>\n      <ul>\n        <li class="right" style="margin-right: 10px">\n          <a href="../genindex.html" title="General Index"\n             accesskey="I">index</a></li>\n        <li class="right" >\n          <a href="../py-modindex.html" title="Python Module Index"\n             >modules</a> |</li>\n        <li class="right" >\n          <a href="controlflow.html" title="4. More Control Flow Tools"\n             accesskey="N">next</a> |</li>\n        <li class="right" >\n          <a href="interpreter.html" title="2. Using the Python Interpreter"\n             accesskey="P">previous</a> |</li>\n        <li><img src="../_static/py.png" alt=""\n                 style="vertical-align: middle; margin-top: -1px"/></li>\n        <li><a href="https://www.python.org/">Python</a> &raquo;</li>\n        <li>\n          <a href="../index.html">3.4.7 Documentation</a> &raquo;\n        </li>\n\n          <li class="nav-item nav-item-1"><a href="index.html" accesskey="U">The Python Tutorial</a> &raquo;</li> \n      </ul>\n    </div>    \n\n    <div class="document">\n      <div class="documentwrapper">\n        <div class="bodywrapper">\n          <div class="body" role="main">\n            \n  <div class="section" id="an-informal-introduction-to-python">\n<span id="tut-informal"></span><h1>3. An Informal Introduction to Python<a class="headerlink" href="#an-informal-introduction-to-python" title="Permalink to this headline">¶</a></h1>\n<p>In the following examples, input and output are distinguished by the presence or\nabsence of prompts (<a class="reference internal" href="../glossary.html#term"><span class="xref std std-term">&gt;&gt;&gt;</span></a> and <a class="reference internal" href="../glossary.html#term-1"><span class="xref std std-term">...</span></a>): to repeat the example, you must type\neverything after the prompt, when the prompt appears; lines that do not begin\nwith a prompt are output from the interpreter. Note that a secondary prompt on a\nline by itself in an example means you must type a blank line; this is used to\nend a multi-line command.</p>\n<p>Many of the examples in this manual, even those entered at the interactive\nprompt, include comments.  Comments in Python start with the hash character,\n<code class="docutils literal"><span class="pre">#</span></code>, and extend to the end of the physical line.  A comment may appear at the\nstart of a line or following whitespace or code, but not within a string\nliteral.  A hash character within a string literal is just a hash character.\nSince comments are to clarify code and are not interpreted by Python, they may\nbe omitted when typing in examples.</p>\n<p>Some examples:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="c1"># this is the first comment</span>\n<span class="n">spam</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># and this is the second comment</span>\n          <span class="c1"># ... and now a third!</span>\n<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;# This is not a comment because it&#39;s inside quotes.&quot;</span>\n</pre></div>\n</div>\n<div class="section" id="using-python-as-a-calculator">\n<span id="tut-calculator"></span><h2>3.1. Using Python as a Calculator<a class="headerlink" href="#using-python-as-a-calculator" title="Permalink to this headline">¶</a></h2>\n<p>Let&#8217;s try some simple Python commands.  Start the interpreter and wait for the\nprimary prompt, <code class="docutils literal"><span class="pre">&gt;&gt;&gt;</span></code>.  (It shouldn&#8217;t take long.)</p>\n<div class="section" id="numbers">\n<span id="tut-numbers"></span><h3>3.1.1. Numbers<a class="headerlink" href="#numbers" title="Permalink to this headline">¶</a></h3>\n<p>The interpreter acts as a simple calculator: you can type an expression at it\nand it will write the value.  Expression syntax is straightforward: the\noperators <code class="docutils literal"><span class="pre">+</span></code>, <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">*</span></code> and <code class="docutils literal"><span class="pre">/</span></code> work just like in most other languages\n(for example, Pascal or C); parentheses (<code class="docutils literal"><span class="pre">()</span></code>) can be used for grouping.\nFor example:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">+</span> <span class="mi">2</span>\n<span class="go">4</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span>\n<span class="go">20</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span>\n<span class="go">5.0</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">8</span> <span class="o">/</span> <span class="mi">5</span>  <span class="c1"># division always returns a floating point number</span>\n<span class="go">1.6</span>\n</pre></div>\n</div>\n<p>The integer numbers (e.g. <code class="docutils literal"><span class="pre">2</span></code>, <code class="docutils literal"><span class="pre">4</span></code>, <code class="docutils literal"><span class="pre">20</span></code>) have type <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a>,\nthe ones with a fractional part (e.g. <code class="docutils literal"><span class="pre">5.0</span></code>, <code class="docutils literal"><span class="pre">1.6</span></code>) have type\n<a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>.  We will see more about numeric types later in the tutorial.</p>\n<p>Division (<code class="docutils literal"><span class="pre">/</span></code>) always returns a float.  To do <a class="reference internal" href="../glossary.html#term-floor-division"><span class="xref std std-term">floor division</span></a> and\nget an integer result (discarding any fractional result) you can use the <code class="docutils literal"><span class="pre">//</span></code>\noperator; to calculate the remainder you can use <code class="docutils literal"><span class="pre">%</span></code>:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">/</span> <span class="mi">3</span>  <span class="c1"># classic division returns a float</span>\n<span class="go">5.666666666666667</span>\n<span class="go">&gt;&gt;&gt;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">//</span> <span class="mi">3</span>  <span class="c1"># floor division discards the fractional part</span>\n<span class="go">5</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">%</span> <span class="mi">3</span>  <span class="c1"># the % operator returns the remainder of the division</span>\n<span class="go">2</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">+</span> <span class="mi">2</span>  <span class="c1"># result * divisor + remainder</span>\n<span class="go">17</span>\n</pre></div>\n</div>\n<p>With Python, it is possible to use the <code class="docutils literal"><span class="pre">**</span></code> operator to calculate powers <a class="footnote-reference" href="#id3" id="id1">[1]</a>:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">**</span> <span class="mi">2</span>  <span class="c1"># 5 squared</span>\n<span class="go">25</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">**</span> <span class="mi">7</span>  <span class="c1"># 2 to the power of 7</span>\n<span class="go">128</span>\n</pre></div>\n</div>\n<p>The equal sign (<code class="docutils literal"><span class="pre">=</span></code>) is used to assign a value to a variable. Afterwards, no\nresult is displayed before the next interactive prompt:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">=</span> <span class="mi">20</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">height</span> <span class="o">=</span> <span class="mi">5</span> <span class="o">*</span> <span class="mi">9</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">*</span> <span class="n">height</span>\n<span class="go">900</span>\n</pre></div>\n</div>\n<p>If a variable is not &#8220;defined&#8221; (assigned a value), trying to use it will\ngive you an error:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">n</span>  <span class="c1"># try to access an undefined variable</span>\n<span class="gt">Traceback (most recent call last):</span>\n  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>\n<span class="gr">NameError</span>: <span class="n">name &#39;n&#39; is not defined</span>\n</pre></div>\n</div>\n<p>There is full support for floating point; operators with mixed type operands\nconvert the integer operand to floating point:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="mf">3.75</span> <span class="o">/</span> <span class="mf">1.5</span>\n<span class="go">7.5</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mf">7.0</span> <span class="o">/</span> <span class="mi">2</span>\n<span class="go">3.5</span>\n</pre></div>\n</div>\n<p>In interactive mode, the last printed expression is assigned to the variable\n<code class="docutils literal"><span class="pre">_</span></code>.  This means that when you are using Python as a desk calculator, it is\nsomewhat easier to continue calculations, for example:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">tax</span> <span class="o">=</span> <span class="mf">12.5</span> <span class="o">/</span> <span class="mi">100</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">=</span> <span class="mf">100.50</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">*</span> <span class="n">tax</span>\n<span class="go">12.5625</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">+</span> <span class="n">_</span>\n<span class="go">113.0625</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>\n<span class="go">113.06</span>\n</pre></div>\n</div>\n<p>This variable should be treated as read-only by the user.  Don&#8217;t explicitly\nassign a value to it &#8212; you would create an independent local variable with the\nsame name masking the built-in variable with its magic behavior.</p>\n<p>In addition to <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> and <a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, Python supports other types of\nnumbers, such as <a class="reference internal" href="../library/decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal"><span class="pre">Decimal</span></code></a> and <a class="reference internal" href="../library/fractions.html#fractions.Fraction" title="fractions.Fraction"><code class="xref py py-class docutils literal"><span class="pre">Fraction</span></code></a>.\nPython also has built-in support for <a class="reference internal" href="../library/stdtypes.html#typesnumeric"><span class="std std-ref">complex numbers</span></a>,\nand uses the <code class="docutils literal"><span class="pre">j</span></code> or <code class="docutils literal"><span class="pre">J</span></code> suffix to indicate the imaginary part\n(e.g. <code class="docutils literal"><span class="pre">3+5j</span></code>).</p>\n</div>\n<div class="section" id="strings">\n<span id="tut-strings"></span><h3>3.1.2. Strings<a class="headerlink" href="#strings" title="Permalink to this headline">¶</a></h3>\n<p>Besides numbers, Python can also manipulate strings, which can be expressed\nin several ways.  They can be enclosed in single quotes (<code class="docutils literal"><span class="pre">\'...\'</span></code>) or\ndouble quotes (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) with the same result <a class="footnote-reference" href="#id4" id="id2">[2]</a>.  <code class="docutils literal"><span class="pre">\\</span></code> can be used\nto escape quotes:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;spam eggs&#39;</span>  <span class="c1"># single quotes</span>\n<span class="go">&#39;spam eggs&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;doesn</span><span class="se">\\&#39;</span><span class="s1">t&#39;</span>  <span class="c1"># use \\&#39; to escape the single quote...</span>\n<span class="go">&quot;doesn&#39;t&quot;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;doesn&#39;t&quot;</span>  <span class="c1"># ...or use double quotes instead</span>\n<span class="go">&quot;doesn&#39;t&quot;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Yes,&quot; he said.&#39;</span>\n<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;</span><span class="se">\\&quot;</span><span class="s2">Yes,</span><span class="se">\\&quot;</span><span class="s2"> he said.&quot;</span>\n<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>\n<span class="go">&#39;&quot;Isn\\&#39;t,&quot; she said.&#39;</span>\n</pre></div>\n</div>\n<p>In the interactive interpreter, the output string is enclosed in quotes and\nspecial characters are escaped with backslashes.  While this might sometimes\nlook different from the input (the enclosing quotes could change), the two\nstrings are equivalent.  The string is enclosed in double quotes if\nthe string contains a single quote and no double quotes, otherwise it is\nenclosed in single quotes.  The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function produces a more\nreadable output, by omitting the enclosing quotes and by printing escaped\nand special characters:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>\n<span class="go">&#39;&quot;Isn\\&#39;t,&quot; she said.&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;&quot;Isn</span><span class="se">\\&#39;</span><span class="s1">t,&quot; she said.&#39;</span><span class="p">)</span>\n<span class="go">&quot;Isn&#39;t,&quot; she said.</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;First line.</span><span class="se">\n</span><span class="s1">Second line.&#39;</span>  <span class="c1"># \n means newline</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span>  <span class="c1"># without print(), \n is included in the output</span>\n<span class="go">&#39;First line.\nSecond line.&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>  <span class="c1"># with print(), \n produces a new line</span>\n<span class="go">First line.</span>\n<span class="go">Second line.</span>\n</pre></div>\n</div>\n<p>If you don&#8217;t want characters prefaced by <code class="docutils literal"><span class="pre">\\</span></code> to be interpreted as\nspecial characters, you can use <em>raw strings</em> by adding an <code class="docutils literal"><span class="pre">r</span></code> before\nthe first quote:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;C:\\some</span><span class="se">\n</span><span class="s1">ame&#39;</span><span class="p">)</span>  <span class="c1"># here \n means newline!</span>\n<span class="go">C:\\some</span>\n<span class="go">ame</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;C:\\some\name&#39;</span><span class="p">)</span>  <span class="c1"># note the r before the quote</span>\n<span class="go">C:\\some\name</span>\n</pre></div>\n</div>\n<p>String literals can span multiple lines.  One way is using triple-quotes:\n<code class="docutils literal"><span class="pre">&quot;&quot;&quot;...&quot;&quot;&quot;</span></code> or <code class="docutils literal"><span class="pre">\'\'\'...\'\'\'</span></code>.  End of lines are automatically\nincluded in the string, but it&#8217;s possible to prevent this by adding a <code class="docutils literal"><span class="pre">\\</span></code> at\nthe end of the line.  The following example:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;&quot;</span><span class="se">\\</span>\n<span class="s2">Usage: thingy [OPTIONS]</span>\n<span class="s2">     -h                        Display this usage message</span>\n<span class="s2">     -H hostname               Hostname to connect to</span>\n<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>\n</pre></div>\n</div>\n<p>produces the following output (note that the initial newline is not included):</p>\n<div class="highlight-text"><div class="highlight"><pre><span></span>Usage: thingy [OPTIONS]\n     -h                        Display this usage message\n     -H hostname               Hostname to connect to\n</pre></div>\n</div>\n<p>Strings can be concatenated (glued together) with the <code class="docutils literal"><span class="pre">+</span></code> operator, and\nrepeated with <code class="docutils literal"><span class="pre">*</span></code>:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># 3 times &#39;un&#39;, followed by &#39;ium&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="s1">&#39;un&#39;</span> <span class="o">+</span> <span class="s1">&#39;ium&#39;</span>\n<span class="go">&#39;unununium&#39;</span>\n</pre></div>\n</div>\n<p>Two or more <em>string literals</em> (i.e. the ones enclosed between quotes) next\nto each other are automatically concatenated.</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Py&#39;</span> <span class="s1">&#39;thon&#39;</span>\n<span class="go">&#39;Python&#39;</span>\n</pre></div>\n</div>\n<p>This only works with two literals though, not with variables or expressions:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">=</span> <span class="s1">&#39;Py&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="s1">&#39;thon&#39;</span>  <span class="c1"># can&#39;t concatenate a variable and a string literal</span>\n<span class="go">  ...</span>\n<span class="go">SyntaxError: invalid syntax</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="s1">&#39;un&#39;</span> <span class="o">*</span> <span class="mi">3</span><span class="p">)</span> <span class="s1">&#39;ium&#39;</span>\n<span class="go">  ...</span>\n<span class="go">SyntaxError: invalid syntax</span>\n</pre></div>\n</div>\n<p>If you want to concatenate variables or a variable and a literal, use <code class="docutils literal"><span class="pre">+</span></code>:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">+</span> <span class="s1">&#39;thon&#39;</span>\n<span class="go">&#39;Python&#39;</span>\n</pre></div>\n</div>\n<p>This feature is particularly useful when you want to break long strings:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">text</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Put several strings within parentheses &#39;</span>\n<span class="go">            &#39;to have them joined together.&#39;)</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">text</span>\n<span class="go">&#39;Put several strings within parentheses to have them joined together.&#39;</span>\n</pre></div>\n</div>\n<p>Strings can be <em>indexed</em> (subscripted), with the first character having index 0.\nThere is no separate character type; a character is simply a string of size\none:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span> <span class="o">=</span> <span class="s1">&#39;Python&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># character in position 0</span>\n<span class="go">&#39;P&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># character in position 5</span>\n<span class="go">&#39;n&#39;</span>\n</pre></div>\n</div>\n<p>Indices may also be negative numbers, to start counting from the right:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>  <span class="c1"># last character</span>\n<span class="go">&#39;n&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># second-last character</span>\n<span class="go">&#39;o&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">6</span><span class="p">]</span>\n<span class="go">&#39;P&#39;</span>\n</pre></div>\n</div>\n<p>Note that since -0 is the same as 0, negative indices start from -1.</p>\n<p>In addition to indexing, <em>slicing</em> is also supported.  While indexing is used\nto obtain individual characters, <em>slicing</em> allows you to obtain substring:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># characters from position 0 (included) to 2 (excluded)</span>\n<span class="go">&#39;Py&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># characters from position 2 (included) to 5 (excluded)</span>\n<span class="go">&#39;tho&#39;</span>\n</pre></div>\n</div>\n<p>Note how the start is always included, and the end always excluded.  This\nmakes sure that <code class="docutils literal"><span class="pre">s[:i]</span> <span class="pre">+</span> <span class="pre">s[i:]</span></code> is always equal to <code class="docutils literal"><span class="pre">s</span></code>:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span>\n<span class="go">&#39;Python&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>\n<span class="go">&#39;Python&#39;</span>\n</pre></div>\n</div>\n<p>Slice indices have useful defaults; an omitted first index defaults to zero, an\nomitted second index defaults to the size of the string being sliced.</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># character from the beginning to position 2 (excluded)</span>\n<span class="go">&#39;Py&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>  <span class="c1"># characters from position 4 (included) to the end</span>\n<span class="go">&#39;on&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="c1"># characters from the second-last (included) to the end</span>\n<span class="go">&#39;on&#39;</span>\n</pre></div>\n</div>\n<p>One way to remember how slices work is to think of the indices as pointing\n<em>between</em> characters, with the left edge of the first character numbered 0.\nThen the right edge of the last character of a string of <em>n</em> characters has\nindex <em>n</em>, for example:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span> <span class="o">+---+---+---+---+---+---+</span>\n <span class="o">|</span> <span class="n">P</span> <span class="o">|</span> <span class="n">y</span> <span class="o">|</span> <span class="n">t</span> <span class="o">|</span> <span class="n">h</span> <span class="o">|</span> <span class="n">o</span> <span class="o">|</span> <span class="n">n</span> <span class="o">|</span>\n <span class="o">+---+---+---+---+---+---+</span>\n <span class="mi">0</span>   <span class="mi">1</span>   <span class="mi">2</span>   <span class="mi">3</span>   <span class="mi">4</span>   <span class="mi">5</span>   <span class="mi">6</span>\n<span class="o">-</span><span class="mi">6</span>  <span class="o">-</span><span class="mi">5</span>  <span class="o">-</span><span class="mi">4</span>  <span class="o">-</span><span class="mi">3</span>  <span class="o">-</span><span class="mi">2</span>  <span class="o">-</span><span class="mi">1</span>\n</pre></div>\n</div>\n<p>The first row of numbers gives the position of the indices 0...6 in the string;\nthe second row gives the corresponding negative indices. The slice from <em>i</em> to\n<em>j</em> consists of all characters between the edges labeled <em>i</em> and <em>j</em>,\nrespectively.</p>\n<p>For non-negative indices, the length of a slice is the difference of the\nindices, if both are within bounds.  For example, the length of <code class="docutils literal"><span class="pre">word[1:3]</span></code> is\n2.</p>\n<p>Attempting to use an index that is too large will result in an error:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">]</span>  <span class="c1"># the word only has 6 characters</span>\n<span class="gt">Traceback (most recent call last):</span>\n  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>\n<span class="gr">IndexError</span>: <span class="n">string index out of range</span>\n</pre></div>\n</div>\n<p>However, out of range slice indexes are handled gracefully when used for\nslicing:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="mi">42</span><span class="p">]</span>\n<span class="go">&#39;on&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">:]</span>\n<span class="go">&#39;&#39;</span>\n</pre></div>\n</div>\n<p>Python strings cannot be changed &#8212; they are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>.\nTherefore, assigning to an indexed position in the string results in an error:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;J&#39;</span>\n<span class="go">  ...</span>\n<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span> <span class="o">=</span> <span class="s1">&#39;py&#39;</span>\n<span class="go">  ...</span>\n<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>\n</pre></div>\n</div>\n<p>If you need a different string, you should create a new one:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;J&#39;</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>\n<span class="go">&#39;Jython&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="s1">&#39;py&#39;</span>\n<span class="go">&#39;Pypy&#39;</span>\n</pre></div>\n</div>\n<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> returns the length of a string:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;supercalifragilisticexpialidocious&#39;</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>\n<span class="go">34</span>\n</pre></div>\n</div>\n<div class="admonition seealso">\n<p class="first admonition-title">See also</p>\n<dl class="last docutils">\n<dt><a class="reference internal" href="../library/stdtypes.html#textseq"><span class="std std-ref">Text Sequence Type &#8212; str</span></a></dt>\n<dd>Strings are examples of <em>sequence types</em>, and support the common\noperations supported by such types.</dd>\n<dt><a class="reference internal" href="../library/stdtypes.html#string-methods"><span class="std std-ref">String Methods</span></a></dt>\n<dd>Strings support a large number of methods for\nbasic transformations and searching.</dd>\n<dt><a class="reference internal" href="../library/string.html#string-formatting"><span class="std std-ref">String Formatting</span></a></dt>\n<dd>Information about string formatting with <a class="reference internal" href="../library/stdtypes.html#str.format" title="str.format"><code class="xref py py-meth docutils literal"><span class="pre">str.format()</span></code></a> is described\nhere.</dd>\n<dt><a class="reference internal" href="../library/stdtypes.html#old-string-formatting"><span class="std std-ref">printf-style String Formatting</span></a></dt>\n<dd>The old formatting operations invoked when strings and Unicode strings are\nthe left operand of the <code class="docutils literal"><span class="pre">%</span></code> operator are described in more detail here.</dd>\n</dl>\n</div>\n</div>\n<div class="section" id="lists">\n<span id="tut-lists"></span><h3>3.1.3. Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h3>\n<p>Python knows a number of <em>compound</em> data types, used to group together other\nvalues.  The most versatile is the <em>list</em>, which can be written as a list of\ncomma-separated values (items) between square brackets.  Lists might contain\nitems of different types, but usually the items all have the same type.</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">25</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span>\n<span class="go">[1, 4, 9, 16, 25]</span>\n</pre></div>\n</div>\n<p>Like strings (and all other built-in <a class="reference internal" href="../glossary.html#term-sequence"><span class="xref std std-term">sequence</span></a> type), lists can be\nindexed and sliced:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># indexing returns the item</span>\n<span class="go">1</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>\n<span class="go">25</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span>  <span class="c1"># slicing returns a new list</span>\n<span class="go">[9, 16, 25]</span>\n</pre></div>\n</div>\n<p>All slice operations return a new list containing the requested elements.  This\nmeans that the following slice returns a new (shallow) copy of the list:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[:]</span>\n<span class="go">[1, 4, 9, 16, 25]</span>\n</pre></div>\n</div>\n<p>Lists also support operations like concatenation:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">+</span> <span class="p">[</span><span class="mi">36</span><span class="p">,</span> <span class="mi">49</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="mi">81</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>\n<span class="go">[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]</span>\n</pre></div>\n</div>\n<p>Unlike strings, which are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>, lists are a <a class="reference internal" href="../glossary.html#term-mutable"><span class="xref std std-term">mutable</span></a>\ntype, i.e. it is possible to change their content:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span> <span class="mi">125</span><span class="p">]</span>  <span class="c1"># something&#39;s wrong here</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="mi">4</span> <span class="o">**</span> <span class="mi">3</span>  <span class="c1"># the cube of 4 is 64, not 65!</span>\n<span class="go">64</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mi">64</span>  <span class="c1"># replace the wrong value</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>\n<span class="go">[1, 8, 27, 64, 125]</span>\n</pre></div>\n</div>\n<p>You can also add new items at the end of the list, by using\nthe <code class="xref py py-meth docutils literal"><span class="pre">append()</span></code> <em>method</em> (we will see more about methods later):</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">216</span><span class="p">)</span>  <span class="c1"># add the cube of 6</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">7</span> <span class="o">**</span> <span class="mi">3</span><span class="p">)</span>  <span class="c1"># and the cube of 7</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>\n<span class="go">[1, 8, 27, 64, 125, 216, 343]</span>\n</pre></div>\n</div>\n<p>Assignment to slices is also possible, and this can even change the size of the\nlist or clear it entirely:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="s1">&#39;e&#39;</span><span class="p">,</span> <span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>\n<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="c1"># replace some values</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;C&#39;</span><span class="p">,</span> <span class="s1">&#39;D&#39;</span><span class="p">,</span> <span class="s1">&#39;E&#39;</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>\n<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;f&#39;, &#39;g&#39;]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="c1"># now remove them</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>\n<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;f&#39;, &#39;g&#39;]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="c1"># clear the list by replacing all the elements with an empty list</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[:]</span> <span class="o">=</span> <span class="p">[]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>\n<span class="go">[]</span>\n</pre></div>\n</div>\n<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> also applies to lists:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">letters</span><span class="p">)</span>\n<span class="go">4</span>\n</pre></div>\n</div>\n<p>It is possible to nest lists (create lists containing other lists), for\nexample:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">n</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span><span class="p">,</span> <span class="n">n</span><span class="p">]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span>\n<span class="go">[[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;], [1, 2, 3]]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>\n<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>\n<span class="go">&#39;b&#39;</span>\n</pre></div>\n</div>\n</div>\n</div>\n<div class="section" id="first-steps-towards-programming">\n<span id="tut-firststeps"></span><h2>3.2. First Steps Towards Programming<a class="headerlink" href="#first-steps-towards-programming" title="Permalink to this headline">¶</a></h2>\n<p>Of course, we can use Python for more complicated tasks than adding two and two\ntogether.  For instance, we can write an initial sub-sequence of the <em>Fibonacci</em>\nseries as follows:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># Fibonacci series:</span>\n<span class="gp">... </span><span class="c1"># the sum of two elements defines the next</span>\n<span class="gp">... </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>\n<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>\n<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>\n<span class="gp">...</span>\n<span class="go">1</span>\n<span class="go">1</span>\n<span class="go">2</span>\n<span class="go">3</span>\n<span class="go">5</span>\n<span class="go">8</span>\n</pre></div>\n</div>\n<p>This example introduces several new features.</p>\n<ul>\n<li><p class="first">The first line contains a <em>multiple assignment</em>: the variables <code class="docutils literal"><span class="pre">a</span></code> and <code class="docutils literal"><span class="pre">b</span></code>\nsimultaneously get the new values 0 and 1.  On the last line this is used again,\ndemonstrating that the expressions on the right-hand side are all evaluated\nfirst before any of the assignments take place.  The right-hand side expressions\nare evaluated  from the left to the right.</p>\n</li>\n<li><p class="first">The <a class="reference internal" href="../reference/compound_stmts.html#while"><code class="xref std std-keyword docutils literal"><span class="pre">while</span></code></a> loop executes as long as the condition (here: <code class="docutils literal"><span class="pre">b</span> <span class="pre">&lt;</span> <span class="pre">10</span></code>)\nremains true.  In Python, like in C, any non-zero integer value is true; zero is\nfalse.  The condition may also be a string or list value, in fact any sequence;\nanything with a non-zero length is true, empty sequences are false.  The test\nused in the example is a simple comparison.  The standard comparison operators\nare written the same as in C: <code class="docutils literal"><span class="pre">&lt;</span></code> (less than), <code class="docutils literal"><span class="pre">&gt;</span></code> (greater than), <code class="docutils literal"><span class="pre">==</span></code>\n(equal to), <code class="docutils literal"><span class="pre">&lt;=</span></code> (less than or equal to), <code class="docutils literal"><span class="pre">&gt;=</span></code> (greater than or equal to)\nand <code class="docutils literal"><span class="pre">!=</span></code> (not equal to).</p>\n</li>\n<li><p class="first">The <em>body</em> of the loop is <em>indented</em>: indentation is Python&#8217;s way of grouping\nstatements.  At the interactive prompt, you have to type a tab or space(s) for\neach indented line.  In practice you will prepare more complicated input\nfor Python with a text editor; all decent text editors have an auto-indent\nfacility.  When a compound statement is entered interactively, it must be\nfollowed by a blank line to indicate completion (since the parser cannot\nguess when you have typed the last line).  Note that each line within a basic\nblock must be indented by the same amount.</p>\n</li>\n<li><p class="first">The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function writes the value of the argument(s) it is given.\nIt differs from just writing the expression you want to write (as we did\nearlier in the calculator examples) in the way it handles multiple arguments,\nfloating point quantities, and strings.  Strings are printed without quotes,\nand a space is inserted between items, so you can format things nicely, like\nthis:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">i</span> <span class="o">=</span> <span class="mi">256</span><span class="o">*</span><span class="mi">256</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;The value of i is&#39;</span><span class="p">,</span> <span class="n">i</span><span class="p">)</span>\n<span class="go">The value of i is 65536</span>\n</pre></div>\n</div>\n<p>The keyword argument <em>end</em> can be used to avoid the newline after the output,\nor end the output with a different string:</p>\n<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>\n<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">1000</span><span class="p">:</span>\n<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>\n<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>\n<span class="gp">...</span>\n<span class="go">1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,</span>\n</pre></div>\n</div>\n</li>\n</ul>\n<p class="rubric">Footnotes</p>\n<table class="docutils footnote" frame="void" id="id3" rules="none">\n<colgroup><col class="label" /><col /></colgroup>\n<tbody valign="top">\n<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>Since <code class="docutils literal"><span class="pre">**</span></code> has higher precedence than <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">-3**2</span></code> will be\ninterpreted as <code class="docutils literal"><span class="pre">-(3**2)</span></code> and thus result in <code class="docutils literal"><span class="pre">-9</span></code>.  To avoid this\nand get <code class="docutils literal"><span class="pre">9</span></code>, you can use <code class="docutils literal"><span class="pre">(-3)**2</span></code>.</td></tr>\n</tbody>\n</table>\n<table class="docutils footnote" frame="void" id="id4" rules="none">\n<colgroup><col class="label" /><col /></colgroup>\n<tbody valign="top">\n<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>Unlike other languages, special characters such as <code class="docutils literal"><span class="pre">\n</span></code> have the\nsame meaning with both single (<code class="docutils literal"><span class="pre">\'...\'</span></code>) and double (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) quotes.\nThe only difference between the two is that within single quotes you don&#8217;t\nneed to escape <code class="docutils literal"><span class="pre">&quot;</span></code> (but you have to escape <code class="docutils literal"><span class="pre">\'</span></code>) and vice versa.</td></tr>\n</tbody>\n</table>\n</div>\n</div>\n\n\n          </div>\n        </div>\n      </div>\n      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">\n        <div class="sphinxsidebarwrapper">\n  <h3><a href="../contents.html">Table Of Contents</a></h3>\n  <ul>\n<li><a class="reference internal" href="#">3. An Informal Introduction to Python</a><ul>\n<li><a class="reference internal" href="#using-python-as-a-calculator">3.1. Using Python as a Calculator</a><ul>\n<li><a class="reference internal" href="#numbers">3.1.1. Numbers</a></li>\n<li><a class="reference internal" href="#strings">3.1.2. Strings</a></li>\n<li><a class="reference internal" href="#lists">3.1.3. Lists</a></li>\n</ul>\n</li>\n<li><a class="reference internal" href="#first-steps-towards-programming">3.2. First Steps Towards Programming</a></li>\n</ul>\n</li>\n</ul>\n\n  <h4>Previous topic</h4>\n  <p class="topless"><a href="interpreter.html"\n                        title="previous chapter">2. Using the Python Interpreter</a></p>\n  <h4>Next topic</h4>\n  <p class="topless"><a href="controlflow.html"\n                        title="next chapter">4. More Control Flow Tools</a></p>\n<h3>This Page</h3>\n<ul class="this-page-menu">\n  <li><a href="../bugs.html">Report a Bug</a></li>\n  <li><a href="../_sources/tutorial/introduction.txt"\n         rel="nofollow">Show Source</a></li>\n</ul>\n\n<div id="searchbox" style="display: none" role="search">\n  <h3>Quick search</h3>\n    <form class="search" action="../search.html" method="get">\n      <div><input type="text" name="q" /></div>\n      <div><input type="submit" value="Go" /></div>\n      <input type="hidden" name="check_keywords" value="yes" />\n      <input type="hidden" name="area" value="default" />\n    </form>\n</div>\n<script type="text/javascript">$(\'#searchbox\').show(0);</script>\n        </div>\n      </div>\n      <div class="clearer"></div>\n    </div>  \n    <div class="related" role="navigation" aria-label="related navigation">\n      <h3>Navigation</h3>\n      <ul>\n        <li class="right" style="margin-right: 10px">\n          <a href="../genindex.html" title="General Index"\n             >index</a></li>\n        <li class="right" >\n          <a href="../py-modindex.html" title="Python Module Index"\n             >modules</a> |</li>\n        <li class="right" >\n          <a href="controlflow.html" title="4. More Control Flow Tools"\n             >next</a> |</li>\n        <li class="right" >\n          <a href="interpreter.html" title="2. Using the Python Interpreter"\n             >previous</a> |</li>\n        <li><img src="../_static/py.png" alt=""\n                 style="vertical-align: middle; margin-top: -1px"/></li>\n        <li><a href="https://www.python.org/">Python</a> &raquo;</li>\n        <li>\n          <a href="../index.html">3.4.7 Documentation</a> &raquo;\n        </li>\n\n          <li class="nav-item nav-item-1"><a href="index.html" >The Python Tutorial</a> &raquo;</li> \n      </ul>\n    </div>  \n    <div class="footer">\n    &copy; <a href="../copyright.html">Copyright</a> 1990-2017, Python Software Foundation.\n    <br />\n    The Python Software Foundation is a non-profit corporation.\n    <a href="https://www.python.org/psf/donations/">Please donate.</a>\n    <br />\n    Last updated on Aug 09, 2017.\n    <a href="../bugs.html">Found a bug</a>?\n    <br />\n    Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.4.4.\n    </div>\n\n  </body>\n  \n</html>'
>>> print (html)

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">


<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    
    <title>3. An Informal Introduction to Python &mdash; Python 3.4.7 documentation</title>
    
    <link rel="stylesheet" href="../_static/pydoctheme.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
    
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    '../',
        VERSION:     '3.4.7',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true
      };
    </script>
    <script type="text/javascript" src="../_static/jquery.js"></script>
    <script type="text/javascript" src="../_static/underscore.js"></script>
    <script type="text/javascript" src="../_static/doctools.js"></script>
    <script type="text/javascript" src="../_static/sidebar.js"></script>
    <link rel="search" type="application/opensearchdescription+xml"
          title="Search within Python 3.4.7 documentation"
          href="../_static/opensearch.xml"/>
    <link rel="author" title="About these documents" href="../about.html" />
    <link rel="copyright" title="Copyright" href="../copyright.html" />
    <link rel="top" title="Python 3.4.7 documentation" href="../contents.html" />
    <link rel="up" title="The Python Tutorial" href="index.html" />
    <link rel="next" title="4. More Control Flow Tools" href="controlflow.html" />
    <link rel="prev" title="2. Using the Python Interpreter" href="interpreter.html" />
    <link rel="shortcut icon" type="image/png" href="../_static/py.png" />
    <script type="text/javascript" src="../_static/copybutton.js"></script>
    
    
 

  </head>
  <body role="document">  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="controlflow.html" title="4. More Control Flow Tools"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="interpreter.html" title="2. Using the Python Interpreter"
             accesskey="P">previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <a href="../index.html">3.4.7 Documentation</a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" accesskey="U">The Python Tutorial</a> &raquo;</li> 
      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <div class="section" id="an-informal-introduction-to-python">
<span id="tut-informal"></span><h1>3. An Informal Introduction to Python<a class="headerlink" href="#an-informal-introduction-to-python" title="Permalink to this headline">¶</a></h1>
<p>In the following examples, input and output are distinguished by the presence or
absence of prompts (<a class="reference internal" href="../glossary.html#term"><span class="xref std std-term">&gt;&gt;&gt;</span></a> and <a class="reference internal" href="../glossary.html#term-1"><span class="xref std std-term">...</span></a>): to repeat the example, you must type
everything after the prompt, when the prompt appears; lines that do not begin
with a prompt are output from the interpreter. Note that a secondary prompt on a
line by itself in an example means you must type a blank line; this is used to
end a multi-line command.</p>
<p>Many of the examples in this manual, even those entered at the interactive
prompt, include comments.  Comments in Python start with the hash character,
<code class="docutils literal"><span class="pre">#</span></code>, and extend to the end of the physical line.  A comment may appear at the
start of a line or following whitespace or code, but not within a string
literal.  A hash character within a string literal is just a hash character.
Since comments are to clarify code and are not interpreted by Python, they may
be omitted when typing in examples.</p>
<p>Some examples:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="c1"># this is the first comment</span>
<span class="n">spam</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># and this is the second comment</span>
          <span class="c1"># ... and now a third!</span>
<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;# This is not a comment because it&#39;s inside quotes.&quot;</span>
</pre></div>
</div>
<div class="section" id="using-python-as-a-calculator">
<span id="tut-calculator"></span><h2>3.1. Using Python as a Calculator<a class="headerlink" href="#using-python-as-a-calculator" title="Permalink to this headline">¶</a></h2>
<p>Let&#8217;s try some simple Python commands.  Start the interpreter and wait for the
primary prompt, <code class="docutils literal"><span class="pre">&gt;&gt;&gt;</span></code>.  (It shouldn&#8217;t take long.)</p>
<div class="section" id="numbers">
<span id="tut-numbers"></span><h3>3.1.1. Numbers<a class="headerlink" href="#numbers" title="Permalink to this headline">¶</a></h3>
<p>The interpreter acts as a simple calculator: you can type an expression at it
and it will write the value.  Expression syntax is straightforward: the
operators <code class="docutils literal"><span class="pre">+</span></code>, <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">*</span></code> and <code class="docutils literal"><span class="pre">/</span></code> work just like in most other languages
(for example, Pascal or C); parentheses (<code class="docutils literal"><span class="pre">()</span></code>) can be used for grouping.
For example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">+</span> <span class="mi">2</span>
<span class="go">4</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span>
<span class="go">20</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="mi">50</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="mi">6</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span>
<span class="go">5.0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">8</span> <span class="o">/</span> <span class="mi">5</span>  <span class="c1"># division always returns a floating point number</span>
<span class="go">1.6</span>
</pre></div>
</div>
<p>The integer numbers (e.g. <code class="docutils literal"><span class="pre">2</span></code>, <code class="docutils literal"><span class="pre">4</span></code>, <code class="docutils literal"><span class="pre">20</span></code>) have type <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a>,
the ones with a fractional part (e.g. <code class="docutils literal"><span class="pre">5.0</span></code>, <code class="docutils literal"><span class="pre">1.6</span></code>) have type
<a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>.  We will see more about numeric types later in the tutorial.</p>
<p>Division (<code class="docutils literal"><span class="pre">/</span></code>) always returns a float.  To do <a class="reference internal" href="../glossary.html#term-floor-division"><span class="xref std std-term">floor division</span></a> and
get an integer result (discarding any fractional result) you can use the <code class="docutils literal"><span class="pre">//</span></code>
operator; to calculate the remainder you can use <code class="docutils literal"><span class="pre">%</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">/</span> <span class="mi">3</span>  <span class="c1"># classic division returns a float</span>
<span class="go">5.666666666666667</span>
<span class="go">&gt;&gt;&gt;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">//</span> <span class="mi">3</span>  <span class="c1"># floor division discards the fractional part</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">17</span> <span class="o">%</span> <span class="mi">3</span>  <span class="c1"># the % operator returns the remainder of the division</span>
<span class="go">2</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">+</span> <span class="mi">2</span>  <span class="c1"># result * divisor + remainder</span>
<span class="go">17</span>
</pre></div>
</div>
<p>With Python, it is possible to use the <code class="docutils literal"><span class="pre">**</span></code> operator to calculate powers <a class="footnote-reference" href="#id3" id="id1">[1]</a>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">5</span> <span class="o">**</span> <span class="mi">2</span>  <span class="c1"># 5 squared</span>
<span class="go">25</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">2</span> <span class="o">**</span> <span class="mi">7</span>  <span class="c1"># 2 to the power of 7</span>
<span class="go">128</span>
</pre></div>
</div>
<p>The equal sign (<code class="docutils literal"><span class="pre">=</span></code>) is used to assign a value to a variable. Afterwards, no
result is displayed before the next interactive prompt:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">=</span> <span class="mi">20</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">height</span> <span class="o">=</span> <span class="mi">5</span> <span class="o">*</span> <span class="mi">9</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">width</span> <span class="o">*</span> <span class="n">height</span>
<span class="go">900</span>
</pre></div>
</div>
<p>If a variable is not &#8220;defined&#8221; (assigned a value), trying to use it will
give you an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">n</span>  <span class="c1"># try to access an undefined variable</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">NameError</span>: <span class="n">name &#39;n&#39; is not defined</span>
</pre></div>
</div>
<p>There is full support for floating point; operators with mixed type operands
convert the integer operand to floating point:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="mf">3.75</span> <span class="o">/</span> <span class="mf">1.5</span>
<span class="go">7.5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mf">7.0</span> <span class="o">/</span> <span class="mi">2</span>
<span class="go">3.5</span>
</pre></div>
</div>
<p>In interactive mode, the last printed expression is assigned to the variable
<code class="docutils literal"><span class="pre">_</span></code>.  This means that when you are using Python as a desk calculator, it is
somewhat easier to continue calculations, for example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">tax</span> <span class="o">=</span> <span class="mf">12.5</span> <span class="o">/</span> <span class="mi">100</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">=</span> <span class="mf">100.50</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">*</span> <span class="n">tax</span>
<span class="go">12.5625</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">price</span> <span class="o">+</span> <span class="n">_</span>
<span class="go">113.0625</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="go">113.06</span>
</pre></div>
</div>
<p>This variable should be treated as read-only by the user.  Don&#8217;t explicitly
assign a value to it &#8212; you would create an independent local variable with the
same name masking the built-in variable with its magic behavior.</p>
<p>In addition to <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal"><span class="pre">int</span></code></a> and <a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal"><span class="pre">float</span></code></a>, Python supports other types of
numbers, such as <a class="reference internal" href="../library/decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal"><span class="pre">Decimal</span></code></a> and <a class="reference internal" href="../library/fractions.html#fractions.Fraction" title="fractions.Fraction"><code class="xref py py-class docutils literal"><span class="pre">Fraction</span></code></a>.
Python also has built-in support for <a class="reference internal" href="../library/stdtypes.html#typesnumeric"><span class="std std-ref">complex numbers</span></a>,
and uses the <code class="docutils literal"><span class="pre">j</span></code> or <code class="docutils literal"><span class="pre">J</span></code> suffix to indicate the imaginary part
(e.g. <code class="docutils literal"><span class="pre">3+5j</span></code>).</p>
</div>
<div class="section" id="strings">
<span id="tut-strings"></span><h3>3.1.2. Strings<a class="headerlink" href="#strings" title="Permalink to this headline">¶</a></h3>
<p>Besides numbers, Python can also manipulate strings, which can be expressed
in several ways.  They can be enclosed in single quotes (<code class="docutils literal"><span class="pre">'...'</span></code>) or
double quotes (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) with the same result <a class="footnote-reference" href="#id4" id="id2">[2]</a>.  <code class="docutils literal"><span class="pre">\</span></code> can be used
to escape quotes:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;spam eggs&#39;</span>  <span class="c1"># single quotes</span>
<span class="go">&#39;spam eggs&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;doesn</span><span class="se">\&#39;</span><span class="s1">t&#39;</span>  <span class="c1"># use \&#39; to escape the single quote...</span>
<span class="go">&quot;doesn&#39;t&quot;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;doesn&#39;t&quot;</span>  <span class="c1"># ...or use double quotes instead</span>
<span class="go">&quot;doesn&#39;t&quot;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">&quot;</span><span class="se">\&quot;</span><span class="s2">Yes,</span><span class="se">\&quot;</span><span class="s2"> he said.&quot;</span>
<span class="go">&#39;&quot;Yes,&quot; he said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>
<span class="go">&#39;&quot;Isn\&#39;t,&quot; she said.&#39;</span>
</pre></div>
</div>
<p>In the interactive interpreter, the output string is enclosed in quotes and
special characters are escaped with backslashes.  While this might sometimes
look different from the input (the enclosing quotes could change), the two
strings are equivalent.  The string is enclosed in double quotes if
the string contains a single quote and no double quotes, otherwise it is
enclosed in single quotes.  The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function produces a more
readable output, by omitting the enclosing quotes and by printing escaped
and special characters:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span>
<span class="go">&#39;&quot;Isn\&#39;t,&quot; she said.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;&quot;Isn</span><span class="se">\&#39;</span><span class="s1">t,&quot; she said.&#39;</span><span class="p">)</span>
<span class="go">&quot;Isn&#39;t,&quot; she said.</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;First line.</span><span class="se">
</span><span class="s1">Second line.&#39;</span>  <span class="c1"># 
 means newline</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span>  <span class="c1"># without print(), 
 is included in the output</span>
<span class="go">&#39;First line.
Second line.&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>  <span class="c1"># with print(), 
 produces a new line</span>
<span class="go">First line.</span>
<span class="go">Second line.</span>
</pre></div>
</div>
<p>If you don&#8217;t want characters prefaced by <code class="docutils literal"><span class="pre">\</span></code> to be interpreted as
special characters, you can use <em>raw strings</em> by adding an <code class="docutils literal"><span class="pre">r</span></code> before
the first quote:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;C:\some</span><span class="se">
</span><span class="s1">ame&#39;</span><span class="p">)</span>  <span class="c1"># here 
 means newline!</span>
<span class="go">C:\some</span>
<span class="go">ame</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;C:\some
ame&#39;</span><span class="p">)</span>  <span class="c1"># note the r before the quote</span>
<span class="go">C:\some
ame</span>
</pre></div>
</div>
<p>String literals can span multiple lines.  One way is using triple-quotes:
<code class="docutils literal"><span class="pre">&quot;&quot;&quot;...&quot;&quot;&quot;</span></code> or <code class="docutils literal"><span class="pre">'''...'''</span></code>.  End of lines are automatically
included in the string, but it&#8217;s possible to prevent this by adding a <code class="docutils literal"><span class="pre">\</span></code> at
the end of the line.  The following example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">Usage: thingy [OPTIONS]</span>
<span class="s2">     -h                        Display this usage message</span>
<span class="s2">     -H hostname               Hostname to connect to</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>produces the following output (note that the initial newline is not included):</p>
<div class="highlight-text"><div class="highlight"><pre><span></span>Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
</pre></div>
</div>
<p>Strings can be concatenated (glued together) with the <code class="docutils literal"><span class="pre">+</span></code> operator, and
repeated with <code class="docutils literal"><span class="pre">*</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># 3 times &#39;un&#39;, followed by &#39;ium&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">3</span> <span class="o">*</span> <span class="s1">&#39;un&#39;</span> <span class="o">+</span> <span class="s1">&#39;ium&#39;</span>
<span class="go">&#39;unununium&#39;</span>
</pre></div>
</div>
<p>Two or more <em>string literals</em> (i.e. the ones enclosed between quotes) next
to each other are automatically concatenated.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;Py&#39;</span> <span class="s1">&#39;thon&#39;</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>This only works with two literals though, not with variables or expressions:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">=</span> <span class="s1">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="s1">&#39;thon&#39;</span>  <span class="c1"># can&#39;t concatenate a variable and a string literal</span>
<span class="go">  ...</span>
<span class="go">SyntaxError: invalid syntax</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">(</span><span class="s1">&#39;un&#39;</span> <span class="o">*</span> <span class="mi">3</span><span class="p">)</span> <span class="s1">&#39;ium&#39;</span>
<span class="go">  ...</span>
<span class="go">SyntaxError: invalid syntax</span>
</pre></div>
</div>
<p>If you want to concatenate variables or a variable and a literal, use <code class="docutils literal"><span class="pre">+</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">prefix</span> <span class="o">+</span> <span class="s1">&#39;thon&#39;</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>This feature is particularly useful when you want to break long strings:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">text</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Put several strings within parentheses &#39;</span>
<span class="go">            &#39;to have them joined together.&#39;)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">text</span>
<span class="go">&#39;Put several strings within parentheses to have them joined together.&#39;</span>
</pre></div>
</div>
<p>Strings can be <em>indexed</em> (subscripted), with the first character having index 0.
There is no separate character type; a character is simply a string of size
one:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span> <span class="o">=</span> <span class="s1">&#39;Python&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># character in position 0</span>
<span class="go">&#39;P&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># character in position 5</span>
<span class="go">&#39;n&#39;</span>
</pre></div>
</div>
<p>Indices may also be negative numbers, to start counting from the right:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>  <span class="c1"># last character</span>
<span class="go">&#39;n&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># second-last character</span>
<span class="go">&#39;o&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">6</span><span class="p">]</span>
<span class="go">&#39;P&#39;</span>
</pre></div>
</div>
<p>Note that since -0 is the same as 0, negative indices start from -1.</p>
<p>In addition to indexing, <em>slicing</em> is also supported.  While indexing is used
to obtain individual characters, <em>slicing</em> allows you to obtain substring:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># characters from position 0 (included) to 2 (excluded)</span>
<span class="go">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span>  <span class="c1"># characters from position 2 (included) to 5 (excluded)</span>
<span class="go">&#39;tho&#39;</span>
</pre></div>
</div>
<p>Note how the start is always included, and the end always excluded.  This
makes sure that <code class="docutils literal"><span class="pre">s[:i]</span> <span class="pre">+</span> <span class="pre">s[i:]</span></code> is always equal to <code class="docutils literal"><span class="pre">s</span></code>:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span>
<span class="go">&#39;Python&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>
<span class="go">&#39;Python&#39;</span>
</pre></div>
</div>
<p>Slice indices have useful defaults; an omitted first index defaults to zero, an
omitted second index defaults to the size of the string being sliced.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span>  <span class="c1"># character from the beginning to position 2 (excluded)</span>
<span class="go">&#39;Py&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span>  <span class="c1"># characters from position 4 (included) to the end</span>
<span class="go">&#39;on&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="c1"># characters from the second-last (included) to the end</span>
<span class="go">&#39;on&#39;</span>
</pre></div>
</div>
<p>One way to remember how slices work is to think of the indices as pointing
<em>between</em> characters, with the left edge of the first character numbered 0.
Then the right edge of the last character of a string of <em>n</em> characters has
index <em>n</em>, for example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span> <span class="o">+---+---+---+---+---+---+</span>
 <span class="o">|</span> <span class="n">P</span> <span class="o">|</span> <span class="n">y</span> <span class="o">|</span> <span class="n">t</span> <span class="o">|</span> <span class="n">h</span> <span class="o">|</span> <span class="n">o</span> <span class="o">|</span> <span class="n">n</span> <span class="o">|</span>
 <span class="o">+---+---+---+---+---+---+</span>
 <span class="mi">0</span>   <span class="mi">1</span>   <span class="mi">2</span>   <span class="mi">3</span>   <span class="mi">4</span>   <span class="mi">5</span>   <span class="mi">6</span>
<span class="o">-</span><span class="mi">6</span>  <span class="o">-</span><span class="mi">5</span>  <span class="o">-</span><span class="mi">4</span>  <span class="o">-</span><span class="mi">3</span>  <span class="o">-</span><span class="mi">2</span>  <span class="o">-</span><span class="mi">1</span>
</pre></div>
</div>
<p>The first row of numbers gives the position of the indices 0...6 in the string;
the second row gives the corresponding negative indices. The slice from <em>i</em> to
<em>j</em> consists of all characters between the edges labeled <em>i</em> and <em>j</em>,
respectively.</p>
<p>For non-negative indices, the length of a slice is the difference of the
indices, if both are within bounds.  For example, the length of <code class="docutils literal"><span class="pre">word[1:3]</span></code> is
2.</p>
<p>Attempting to use an index that is too large will result in an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">]</span>  <span class="c1"># the word only has 6 characters</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">IndexError</span>: <span class="n">string index out of range</span>
</pre></div>
</div>
<p>However, out of range slice indexes are handled gracefully when used for
slicing:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="mi">42</span><span class="p">]</span>
<span class="go">&#39;on&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">42</span><span class="p">:]</span>
<span class="go">&#39;&#39;</span>
</pre></div>
</div>
<p>Python strings cannot be changed &#8212; they are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>.
Therefore, assigning to an indexed position in the string results in an error:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;J&#39;</span>
<span class="go">  ...</span>
<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[</span><span class="mi">2</span><span class="p">:]</span> <span class="o">=</span> <span class="s1">&#39;py&#39;</span>
<span class="go">  ...</span>
<span class="go">TypeError: &#39;str&#39; object does not support item assignment</span>
</pre></div>
</div>
<p>If you need a different string, you should create a new one:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">&#39;J&#39;</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<span class="go">&#39;Jython&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">word</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="s1">&#39;py&#39;</span>
<span class="go">&#39;Pypy&#39;</span>
</pre></div>
</div>
<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> returns the length of a string:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;supercalifragilisticexpialidocious&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<span class="go">34</span>
</pre></div>
</div>
<div class="admonition seealso">
<p class="first admonition-title">See also</p>
<dl class="last docutils">
<dt><a class="reference internal" href="../library/stdtypes.html#textseq"><span class="std std-ref">Text Sequence Type &#8212; str</span></a></dt>
<dd>Strings are examples of <em>sequence types</em>, and support the common
operations supported by such types.</dd>
<dt><a class="reference internal" href="../library/stdtypes.html#string-methods"><span class="std std-ref">String Methods</span></a></dt>
<dd>Strings support a large number of methods for
basic transformations and searching.</dd>
<dt><a class="reference internal" href="../library/string.html#string-formatting"><span class="std std-ref">String Formatting</span></a></dt>
<dd>Information about string formatting with <a class="reference internal" href="../library/stdtypes.html#str.format" title="str.format"><code class="xref py py-meth docutils literal"><span class="pre">str.format()</span></code></a> is described
here.</dd>
<dt><a class="reference internal" href="../library/stdtypes.html#old-string-formatting"><span class="std std-ref">printf-style String Formatting</span></a></dt>
<dd>The old formatting operations invoked when strings and Unicode strings are
the left operand of the <code class="docutils literal"><span class="pre">%</span></code> operator are described in more detail here.</dd>
</dl>
</div>
</div>
<div class="section" id="lists">
<span id="tut-lists"></span><h3>3.1.3. Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h3>
<p>Python knows a number of <em>compound</em> data types, used to group together other
values.  The most versatile is the <em>list</em>, which can be written as a list of
comma-separated values (items) between square brackets.  Lists might contain
items of different types, but usually the items all have the same type.</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">25</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span>
<span class="go">[1, 4, 9, 16, 25]</span>
</pre></div>
</div>
<p>Like strings (and all other built-in <a class="reference internal" href="../glossary.html#term-sequence"><span class="xref std std-term">sequence</span></a> type), lists can be
indexed and sliced:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># indexing returns the item</span>
<span class="go">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">25</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span>  <span class="c1"># slicing returns a new list</span>
<span class="go">[9, 16, 25]</span>
</pre></div>
</div>
<p>All slice operations return a new list containing the requested elements.  This
means that the following slice returns a new (shallow) copy of the list:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span><span class="p">[:]</span>
<span class="go">[1, 4, 9, 16, 25]</span>
</pre></div>
</div>
<p>Lists also support operations like concatenation:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">squares</span> <span class="o">+</span> <span class="p">[</span><span class="mi">36</span><span class="p">,</span> <span class="mi">49</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="mi">81</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>
<span class="go">[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]</span>
</pre></div>
</div>
<p>Unlike strings, which are <a class="reference internal" href="../glossary.html#term-immutable"><span class="xref std std-term">immutable</span></a>, lists are a <a class="reference internal" href="../glossary.html#term-mutable"><span class="xref std std-term">mutable</span></a>
type, i.e. it is possible to change their content:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span> <span class="mi">125</span><span class="p">]</span>  <span class="c1"># something&#39;s wrong here</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">4</span> <span class="o">**</span> <span class="mi">3</span>  <span class="c1"># the cube of 4 is 64, not 65!</span>
<span class="go">64</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mi">64</span>  <span class="c1"># replace the wrong value</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>
<span class="go">[1, 8, 27, 64, 125]</span>
</pre></div>
</div>
<p>You can also add new items at the end of the list, by using
the <code class="xref py py-meth docutils literal"><span class="pre">append()</span></code> <em>method</em> (we will see more about methods later):</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">216</span><span class="p">)</span>  <span class="c1"># add the cube of 6</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">7</span> <span class="o">**</span> <span class="mi">3</span><span class="p">)</span>  <span class="c1"># and the cube of 7</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">cubes</span>
<span class="go">[1, 8, 27, 64, 125, 216, 343]</span>
</pre></div>
</div>
<p>Assignment to slices is also possible, and this can even change the size of the
list or clear it entirely:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="s1">&#39;e&#39;</span><span class="p">,</span> <span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># replace some values</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;C&#39;</span><span class="p">,</span> <span class="s1">&#39;D&#39;</span><span class="p">,</span> <span class="s1">&#39;E&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># now remove them</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;f&#39;, &#39;g&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># clear the list by replacing all the elements with an empty list</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span><span class="p">[:]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span>
<span class="go">[]</span>
</pre></div>
</div>
<p>The built-in function <a class="reference internal" href="../library/functions.html#len" title="len"><code class="xref py py-func docutils literal"><span class="pre">len()</span></code></a> also applies to lists:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">letters</span><span class="p">)</span>
<span class="go">4</span>
</pre></div>
</div>
<p>It is possible to nest lists (create lists containing other lists), for
example:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">n</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span><span class="p">,</span> <span class="n">n</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span>
<span class="go">[[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;], [1, 2, 3]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
<span class="go">&#39;b&#39;</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="first-steps-towards-programming">
<span id="tut-firststeps"></span><h2>3.2. First Steps Towards Programming<a class="headerlink" href="#first-steps-towards-programming" title="Permalink to this headline">¶</a></h2>
<p>Of course, we can use Python for more complicated tasks than adding two and two
together.  For instance, we can write an initial sub-sequence of the <em>Fibonacci</em>
series as follows:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="c1"># Fibonacci series:</span>
<span class="gp">... </span><span class="c1"># the sum of two elements defines the next</span>
<span class="gp">... </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">)</span>
<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
<span class="gp">...</span>
<span class="go">1</span>
<span class="go">1</span>
<span class="go">2</span>
<span class="go">3</span>
<span class="go">5</span>
<span class="go">8</span>
</pre></div>
</div>
<p>This example introduces several new features.</p>
<ul>
<li><p class="first">The first line contains a <em>multiple assignment</em>: the variables <code class="docutils literal"><span class="pre">a</span></code> and <code class="docutils literal"><span class="pre">b</span></code>
simultaneously get the new values 0 and 1.  On the last line this is used again,
demonstrating that the expressions on the right-hand side are all evaluated
first before any of the assignments take place.  The right-hand side expressions
are evaluated  from the left to the right.</p>
</li>
<li><p class="first">The <a class="reference internal" href="../reference/compound_stmts.html#while"><code class="xref std std-keyword docutils literal"><span class="pre">while</span></code></a> loop executes as long as the condition (here: <code class="docutils literal"><span class="pre">b</span> <span class="pre">&lt;</span> <span class="pre">10</span></code>)
remains true.  In Python, like in C, any non-zero integer value is true; zero is
false.  The condition may also be a string or list value, in fact any sequence;
anything with a non-zero length is true, empty sequences are false.  The test
used in the example is a simple comparison.  The standard comparison operators
are written the same as in C: <code class="docutils literal"><span class="pre">&lt;</span></code> (less than), <code class="docutils literal"><span class="pre">&gt;</span></code> (greater than), <code class="docutils literal"><span class="pre">==</span></code>
(equal to), <code class="docutils literal"><span class="pre">&lt;=</span></code> (less than or equal to), <code class="docutils literal"><span class="pre">&gt;=</span></code> (greater than or equal to)
and <code class="docutils literal"><span class="pre">!=</span></code> (not equal to).</p>
</li>
<li><p class="first">The <em>body</em> of the loop is <em>indented</em>: indentation is Python&#8217;s way of grouping
statements.  At the interactive prompt, you have to type a tab or space(s) for
each indented line.  In practice you will prepare more complicated input
for Python with a text editor; all decent text editors have an auto-indent
facility.  When a compound statement is entered interactively, it must be
followed by a blank line to indicate completion (since the parser cannot
guess when you have typed the last line).  Note that each line within a basic
block must be indented by the same amount.</p>
</li>
<li><p class="first">The <a class="reference internal" href="../library/functions.html#print" title="print"><code class="xref py py-func docutils literal"><span class="pre">print()</span></code></a> function writes the value of the argument(s) it is given.
It differs from just writing the expression you want to write (as we did
earlier in the calculator examples) in the way it handles multiple arguments,
floating point quantities, and strings.  Strings are printed without quotes,
and a space is inserted between items, so you can format things nicely, like
this:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">i</span> <span class="o">=</span> <span class="mi">256</span><span class="o">*</span><span class="mi">256</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;The value of i is&#39;</span><span class="p">,</span> <span class="n">i</span><span class="p">)</span>
<span class="go">The value of i is 65536</span>
</pre></div>
</div>
<p>The keyword argument <em>end</em> can be used to avoid the newline after the output,
or end the output with a different string:</p>
<div class="highlight-python3"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">while</span> <span class="n">b</span> <span class="o">&lt;</span> <span class="mi">1000</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="gp">... </span>    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
<span class="gp">...</span>
<span class="go">1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,</span>
</pre></div>
</div>
</li>
</ul>
<p class="rubric">Footnotes</p>
<table class="docutils footnote" frame="void" id="id3" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>Since <code class="docutils literal"><span class="pre">**</span></code> has higher precedence than <code class="docutils literal"><span class="pre">-</span></code>, <code class="docutils literal"><span class="pre">-3**2</span></code> will be
interpreted as <code class="docutils literal"><span class="pre">-(3**2)</span></code> and thus result in <code class="docutils literal"><span class="pre">-9</span></code>.  To avoid this
and get <code class="docutils literal"><span class="pre">9</span></code>, you can use <code class="docutils literal"><span class="pre">(-3)**2</span></code>.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id4" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>Unlike other languages, special characters such as <code class="docutils literal"><span class="pre">
</span></code> have the
same meaning with both single (<code class="docutils literal"><span class="pre">'...'</span></code>) and double (<code class="docutils literal"><span class="pre">&quot;...&quot;</span></code>) quotes.
The only difference between the two is that within single quotes you don&#8217;t
need to escape <code class="docutils literal"><span class="pre">&quot;</span></code> (but you have to escape <code class="docutils literal"><span class="pre">'</span></code>) and vice versa.</td></tr>
</tbody>
</table>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h3><a href="../contents.html">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#">3. An Informal Introduction to Python</a><ul>
<li><a class="reference internal" href="#using-python-as-a-calculator">3.1. Using Python as a Calculator</a><ul>
<li><a class="reference internal" href="#numbers">3.1.1. Numbers</a></li>
<li><a class="reference internal" href="#strings">3.1.2. Strings</a></li>
<li><a class="reference internal" href="#lists">3.1.3. Lists</a></li>
</ul>
</li>
<li><a class="reference internal" href="#first-steps-towards-programming">3.2. First Steps Towards Programming</a></li>
</ul>
</li>
</ul>

  <h4>Previous topic</h4>
  <p class="topless"><a href="interpreter.html"
                        title="previous chapter">2. Using the Python Interpreter</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="controlflow.html"
                        title="next chapter">4. More Control Flow Tools</a></p>
<h3>This Page</h3>
<ul class="this-page-menu">
  <li><a href="../bugs.html">Report a Bug</a></li>
  <li><a href="../_sources/tutorial/introduction.txt"
         rel="nofollow">Show Source</a></li>
</ul>

<div id="searchbox" style="display: none" role="search">
  <h3>Quick search</h3>
    <form class="search" action="../search.html" method="get">
      <div><input type="text" name="q" /></div>
      <div><input type="submit" value="Go" /></div>
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="right" >
          <a href="controlflow.html" title="4. More Control Flow Tools"
             >next</a> |</li>
        <li class="right" >
          <a href="interpreter.html" title="2. Using the Python Interpreter"
             >previous</a> |</li>
        <li><img src="../_static/py.png" alt=""
                 style="vertical-align: middle; margin-top: -1px"/></li>
        <li><a href="https://www.python.org/">Python</a> &raquo;</li>
        <li>
          <a href="../index.html">3.4.7 Documentation</a> &raquo;
        </li>

          <li class="nav-item nav-item-1"><a href="index.html" >The Python Tutorial</a> &raquo;</li> 
      </ul>
    </div>  
    <div class="footer">
    &copy; <a href="../copyright.html">Copyright</a> 1990-2017, Python Software Foundation.
    <br />
    The Python Software Foundation is a non-profit corporation.
    <a href="https://www.python.org/psf/donations/">Please donate.</a>
    <br />
    Last updated on Aug 09, 2017.
    <a href="../bugs.html">Found a bug</a>?
    <br />
    Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.4.4.
    </div>

  </body>
  
</html>
>>> 
