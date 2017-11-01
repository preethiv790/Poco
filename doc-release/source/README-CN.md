

<!DOCTYPE html>
<!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
<head>
  <meta charset="utf-8">
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Poco ポコ &mdash; poco  documentation</title>
  

  
  
  
  

  

  
  
    

  

  
  
    <link rel="stylesheet" href="../_static/css/theme.css" type="text/css" />
  

  

  
        <link rel="index" title="Index"
              href="../genindex.html"/>
        <link rel="search" title="Search" href="../search.html"/>
    <link rel="top" title="poco  documentation" href="../index.html"/> 

  
  <script src="../_static/js/modernizr.min.js"></script>

</head>

<body class="wy-body-for-nav" role="document">

   
  <div class="wy-grid-for-nav">

    
    <nav data-toggle="wy-nav-shift" class="wy-nav-side">
      <div class="wy-side-scroll">
        <div class="wy-side-nav-search">
          

          
            <a href="../index.html" class="icon icon-home"> poco
          

          
          </a>

          
            
            
          

          
<div role="search">
  <form id="rtd-search-form" class="wy-form" action="../search.html" method="get">
    <input type="text" name="q" placeholder="Search docs" />
    <input type="hidden" name="check_keywords" value="yes" />
    <input type="hidden" name="area" value="default" />
  </form>
</div>

          
        </div>

        <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="main navigation">
          
            
            
              
            
            
              <ul>
<li class="toctree-l1"><a class="reference internal" href="README.html">Poco ポコ</a></li>
</ul>
<ul>
<li class="toctree-l1"><a class="reference internal" href="poco.html">poco package</a></li>
<li class="toctree-l1"><a class="reference internal" href="poco.proxy.html">poco.proxy module</a></li>
<li class="toctree-l1"><a class="reference internal" href="poco.exceptions.html">poco.exceptions module</a></li>
</ul>
<ul>
<li class="toctree-l1"><a class="reference internal" href="poco.sdk.html">poco.sdk package</a></li>
<li class="toctree-l1"><a class="reference internal" href="poco.sdk.interfaces.html">poco.sdk.interfaces package</a></li>
</ul>

            
          
        </div>
      </div>
    </nav>

    <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">

      
      <nav class="wy-nav-top" role="navigation" aria-label="top navigation">
        
          <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
          <a href="../index.html">poco</a>
        
      </nav>


      
      <div class="wy-nav-content">
        <div class="rst-content">
          















<div role="navigation" aria-label="breadcrumbs navigation">

  <ul class="wy-breadcrumbs">
    
      <li><a href="../index.html">Docs</a> &raquo;</li>
        
      <li>Poco ポコ</li>
    
    
      <li class="wy-breadcrumbs-aside">
        
            
            <a href="../_sources/source/README-CN.md.txt" rel="nofollow"> View page source</a>
          
        
      </li>
    
  </ul>

  
  <hr/>
</div>
          <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
           <div itemprop="articleBody">
            
  <div class="section" id="poco">
<span id="poco"></span><h1>Poco ポコ<a class="headerlink" href="#poco" title="Permalink to this headline">¶</a></h1>
<p><strong>A cross-engine UI automation framework</strong></p>
<p><a class="reference external" href="README.md">English README</a> here.</p>
<!-- chinese only --><p>一个引擎无关的自动化框架。通过HunterRpc进行数据传输，所有接入了<a class="reference external" href="http://hunter.nie.netease.com">hunter</a>的项目可直接使用该测试框架。</p>
<div class="section" id="notice">
<span id="notice"></span><h2>提醒(notice)<a class="headerlink" href="#notice" title="Permalink to this headline">¶</a></h2>
<p>UI自动化有风险，请务必等待UI freeze阶段后再投入生产和使用。</p>
<!-- end of chinese only --></div>
<div class="section" id="installation">
<span id="installation"></span><h2>安装(installation)<a class="headerlink" href="#installation" title="Permalink to this headline">¶</a></h2>
<div class="highlight-sh"><div class="highlight"><pre><span></span><span class="c1"># airtest runtime</span>
git clone ssh://git@git-qa.gz.netease.com:32200/gzliuxin/airtest.git
pip install -e airtest

<span class="c1"># aircv for airtest</span>
git clone -b open-source ssh://git@git-qa.gz.netease.com:32200/airtest-projects/aircv.git
pip install -e aircv

<span class="c1"># hrpc</span>
git clone ssh://git@git-qa.gz.netease.com:32200/maki/hrpc.git
pip install -e hrpc

<span class="c1"># hunter-cli</span>
git clone ssh://git@git-qa.gz.netease.com:32200/maki/hunter-cli.git
pip install -e hunter-cli

<span class="c1"># hunter lib for airtest</span>
git clone ssh://git@git-qa.gz.netease.com:32200/maki/airtest-hunter.git
pip install -e airtest-hunter

<span class="c1"># poco</span>
git clone ssh://git@git-qa.gz.netease.com:32200/maki/poco.git
pip install -e poco

<span class="c1"># poco unittest framework</span>
git clone ssh://git@git-qa.gz.netease.com:32200/maki/PocoUnit.git
pip install -e PocoUnit
</pre></div>
</div>
<!-- chinese only --><p>安装遇到权限问题请下载我们的<a class="reference external" href="http://init.nie.netease.com/downloads/deploy/deploy-key">deploy-key</a>，将下载下来的deploy-key放到 <code class="docutils literal"><span class="pre">C:\User\&lt;username&gt;\.ssh\</span></code> 目录下，改名为<code class="docutils literal"><span class="pre">id_rsa</span></code>，再重新运行上面的命令。</p>
<!-- end of chinese only --></div>
<div class="section" id="concepts">
<span id="concepts"></span><h2>基本概念(concepts)<a class="headerlink" href="#concepts" title="Permalink to this headline">¶</a></h2>
<!-- chinese only --><div class="section" id="">
<span id="id1"></span><h3>测试<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p><strong>TestCase</strong>: 无论以何种形式表示的测试内容的一个单元，以下均指使用Poco编写的测试脚本<strong>TestSuite</strong>: 多个TestCase或TestSuite构成的一系列脚本文件<strong>TestRunner</strong>: 用于启动测试的一个东西，可能是一个可执行文件也可以是一个class。Poco默认使用Airtest作为TestRunner，使用Airtest启动的测试需要安装Airtest环境<strong>TestTarget/TargetDevice</strong>: 运行待测应用程序的设备，以下均指运行在手机上的待测游戏或PC版待测游戏</p>
<p><strong>TestFramework</strong>:  测试框架，Poco就是一个测试框架<strong>TestFrameworkSDK</strong>:  测试框架与待测应用集成的模块，一般来说不是必须的，Poco里带有一个SDK</p>
<!-- end of chinese only --></div>
<div class="section" id="poco">
<span id="id2"></span><h3>Poco测试框架相关<a class="headerlink" href="#poco" title="Permalink to this headline">¶</a></h3>
<p><strong>目标设备</strong>: 待测应用或游戏运行的机器，一般指手机<strong>UI代理(UI proxy)</strong>: poco框架内代表游戏内0个1个或多个UI元素的代理对象<strong>节点/UI元素(Node/UI element)</strong>: 应用/游戏内UI元素的实例，就是平时所说的UI<strong>选择器(选择表达式)(query condition/expression)</strong>: 一个可序列化的数据结构，poco通过该表达式与<strong>目标设备</strong>交互并选出其代表的对应的UI元素。Tester一般不用关心这个表达式的内部结构，除非要自定义<code class="docutils literal"><span class="pre">Selector</span></code>类。</p>
<p><img alt="image" src="../_images/hunter-inspector.png" />
<img alt="image" src="../_images/hunter-inspector-text-attribute.png" />
<img alt="image" src="../_images/hunter-inspector-hierarchy-relations.png" /></p>
</div>
<div class="section" id="">
<span id="id3"></span><h3>坐标系与度量空间定义<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p><img alt="image" src="../_images/hunter-poco-coordinate-system.png" /></p>
<div class="section" id="">
<span id="id4"></span><h4>归一化坐标系<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h4>
<p>归一化坐标系就是将屏幕宽和高按照单位一来算，这样UI在poco中的宽和高其实就是相对于屏幕的百分比大小了，好处就是不同分辨率设备之间，同一个UI的归一化坐标系下的位置和尺寸是一样的，有助于编写跨设备测试用例。</p>
<p>归一化坐标系的空间是均匀的，屏幕正中央一定是(0.5, 0.5)，其他标量和向量的计算方法同欧式空间。</p>
</div>
<div class="section" id="">
<span id="id5"></span><h4>局部坐标系（局部定位）<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h4>
<p>引入局部坐标系是为了表示相对于某UI的坐标。局部坐标系以UI包围盒左上角为原点，向右为x轴，向下为y轴，包围盒宽和高均为单位一。其余的定义和归一化坐标系类似。</p>
<p>局部坐标系可以更灵活地定位UI内或外的位置，例如(0.5, 0.5)就代表UI的正中央，超过1或小于0的坐标值则表示UI的外面。</p>
</div>
</div>
</div>
<div class="section" id="">
<span id="id6"></span><h2>对象选择与操作<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h2>
<div class="section" id="">
<span id="id7"></span><h3>选择器实例初始化<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p>不用引擎版本的poco的实例化方式有点不一样，以下以Unity3D为例，其余的请参考：</p>
<ul class="simple">
<li><a class="reference external" href="#">cocos2dx-js</a></li>
<li><a class="reference external" href="#">android-native</a></li>
<li>unreal (开发中)</li>
<li>(others see <a class="reference external" href="#">INTEGRATION guide</a> for more details)</li>
</ul>
<!-- chinese only -->
* [NetEase Internal Engines]() 公司内所有引擎请点此链接
<!-- end of chinese only --><div class="highlight-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">poco.vendor.unity3d</span> <span class="kn">import</span> <span class="n">UnityPoco</span>

<span class="n">poco</span> <span class="o">=</span> <span class="n">UnityPoco</span><span class="p">()</span>
<span class="n">ui</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;...&#39;</span><span class="p">)</span>
</pre></div>
</div>
</div>
<div class="section" id="">
<span id="id8"></span><h3>基本选择器<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p><code class="docutils literal"><span class="pre">poco</span></code>对象的<code class="docutils literal"><span class="pre">__call__</span></code>方法就是进行选择，遍历整个渲染树形结构，选出所有满足给定的属性的对象代理。第一个参数为节点名，其余的属性键值对通过命名参数传入。具体可参考API Reference。</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="c1"># 根据节点名选择</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span>

<span class="c1"># 节点名和属性选择</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s1">&#39;Button&#39;</span><span class="p">)</span>
<span class="n">poco</span><span class="p">(</span><span class="n">textMatches</span><span class="o">=</span><span class="s1">&#39;^据点.*$&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s1">&#39;Button&#39;</span><span class="p">,</span> <span class="n">enable</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-select-simple.png" /></p>
</div>
<div class="section" id="">
<span id="id9"></span><h3>相对选择器<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p>直接通过节点名或节点类型选择的对象容易产生歧义或无法选择时，可通过相对的方式按层级进行选择</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="c1"># 直系孩子/后代选择</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;main_node&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;list_item&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">offspring</span><span class="p">(</span><span class="s1">&#39;item&#39;</span><span class="p">)</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-select-relative.png" /></p>
</div>
<div class="section" id="">
<span id="id10"></span><h3>顺序选择器（索引选择器，更推荐迭代遍历）<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<p>索引和遍历会默认按照从左到右从上到下的空间顺序按顺序遍历。遍历过程中，还未遍历到的节点如果从画面中移除了则会抛出异常，已遍历的节点即使移除也不受影响。遍历顺序在遍历开始前已经确定，遍历过程中界面上的节点进行了重排则仍然按照之前的顺序进行遍历。</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">items</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;main_node&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;list_item&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">offspring</span><span class="p">(</span><span class="s1">&#39;item&#39;</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;material_name&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">get_text</span><span class="p">())</span>
<span class="k">print</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;material_name&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">get_text</span><span class="p">())</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-select-sequence.png" /></p>
</div>
<div class="section" id="">
<span id="id11"></span><h3>遍历对象集合<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="c1"># 遍历每一个商品</span>
<span class="n">items</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;main_node&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;list_item&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">offspring</span><span class="p">(</span><span class="s1">&#39;item&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
    <span class="n">item</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;icn_item&#39;</span><span class="p">)</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-iteration.png" /></p>
</div>
<div class="section" id="">
<span id="id12"></span><h3>获取对象代理属性<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">mission_btn</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="n">mission_btn</span><span class="o">.</span><span class="n">attr</span><span class="p">(</span><span class="s1">&#39;type&#39;</span><span class="p">))</span>  <span class="c1"># &#39;Button&#39;</span>
<span class="k">print</span><span class="p">(</span><span class="n">mission_btn</span><span class="o">.</span><span class="n">get_text</span><span class="p">())</span>  <span class="c1"># &#39;据点支援&#39;</span>
<span class="k">print</span><span class="p">(</span><span class="n">mission_btn</span><span class="o">.</span><span class="n">attr</span><span class="p">(</span><span class="s1">&#39;text&#39;</span><span class="p">))</span>  <span class="c1"># &#39;据点支援&#39;，与get_text方法等价</span>
<span class="k">print</span><span class="p">(</span><span class="n">mission_btn</span><span class="o">.</span><span class="n">exists</span><span class="p">())</span>  <span class="c1"># True，表示是否存在界面中</span>
</pre></div>
</div>
</div>
<div class="section" id="">
<span id="id13"></span><h3>对象代理操作<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h3>
<div class="section" id="click">
<span id="click"></span><h4>click<a class="headerlink" href="#click" title="Permalink to this headline">¶</a></h4>
<p>点击对象，默认以锚点(挂接点)(anchorPoint)对象为点击点。第一个参数传入点击相对位置，对象包围盒左上角为<code class="docutils literal"><span class="pre">[0,</span> <span class="pre">0]</span></code>，右下角为<code class="docutils literal"><span class="pre">[1,</span> <span class="pre">1]</span></code>。偏移范围可以比0小也可以比1大，超过0~1的范围表示超出包围盒范围。</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">click</span><span class="p">()</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">click</span><span class="p">(</span><span class="s1">&#39;center&#39;</span><span class="p">)</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">click</span><span class="p">([</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">])</span>    <span class="c1"># 等价于center</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">focus</span><span class="p">([</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">])</span><span class="o">.</span><span class="n">click</span><span class="p">()</span>  <span class="c1"># 等价于上面的表达式</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-click.png" /></p>
</div>
<div class="section" id="swipe">
<span id="swipe"></span><h4>swipe<a class="headerlink" href="#swipe" title="Permalink to this headline">¶</a></h4>
<p>以对象anchor为起点，朝某个方向滑动一段距离</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">joystick</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;movetouch_panel&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">child</span><span class="p">(</span><span class="s1">&#39;point_img&#39;</span><span class="p">)</span>
<span class="n">joystick</span><span class="o">.</span><span class="n">swipe</span><span class="p">(</span><span class="s1">&#39;up&#39;</span><span class="p">)</span>
<span class="n">joystick</span><span class="o">.</span><span class="n">swipe</span><span class="p">([</span><span class="mf">0.2</span><span class="p">,</span> <span class="o">-</span><span class="mf">0.2</span><span class="p">])</span>  <span class="c1"># 向右上方45度滑动sqrt(0.08)单位距离</span>
<span class="n">joystick</span><span class="o">.</span><span class="n">swipe</span><span class="p">([</span><span class="mf">0.2</span><span class="p">,</span> <span class="o">-</span><span class="mf">0.2</span><span class="p">],</span> <span class="n">duration</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-swipe.png" /></p>
</div>
<div class="section" id="drag">
<span id="drag"></span><h4>drag<a class="headerlink" href="#drag" title="Permalink to this headline">¶</a></h4>
<p>从当前对象拖拽到目标对象</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">poco</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s1">&#39;突破芯片&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">drag_to</span><span class="p">(</span><span class="n">poco</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s1">&#39;岩石司康饼&#39;</span><span class="p">))</span>
</pre></div>
</div>
<p><img alt="image" src="../_images/hunter-poco-drag.png" /></p>
</div>
<div class="section" id="focus">
<span id="focus"></span><h4>focus (局部定位)<a class="headerlink" href="#focus" title="Permalink to this headline">¶</a></h4>
<p>与节点坐标相关的操作默认以anchor为起始点，click的话就直接click在anchor上。如果要进行局部的点击偏移，可以使用focus操作。focus同屏幕坐标系类似，以节点包围盒左上角为原点，长宽均为1，中心点即为<code class="docutils literal"><span class="pre">[0.5,</span> <span class="pre">0.5]</span></code>，右下角为<code class="docutils literal"><span class="pre">[1,</span> <span class="pre">1]</span></code>，以此类推。</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">focus</span><span class="p">(</span><span class="s1">&#39;center&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">click</span><span class="p">()</span>  <span class="c1"># 点击中心点</span>
</pre></div>
</div>
<p>focus也可以用于一个对象的内部定位，例如实现一个ScrollView的卷动操作</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">scrollView</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="s1">&#39;ScollView&#39;</span><span class="p">)</span>
<span class="n">scrollView</span><span class="o">.</span><span class="n">focus</span><span class="p">([</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">])</span><span class="o">.</span><span class="n">drag_to</span><span class="p">(</span><span class="n">scrollView</span><span class="o">.</span><span class="n">focus</span><span class="p">([</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.2</span><span class="p">]))</span>
</pre></div>
</div>
</div>
<div class="section" id="wait">
<span id="wait"></span><h4>wait<a class="headerlink" href="#wait" title="Permalink to this headline">¶</a></h4>
<p>等待目标对象出现，总是返回对象自身，如果出现立即返回，否则timeout后返回</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span><span class="o">.</span><span class="n">click</span><span class="p">()</span>  <span class="c1"># 最多等待5秒，出现即点击</span>
<span class="n">poco</span><span class="p">(</span><span class="s1">&#39;bg_mission&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span><span class="o">.</span><span class="n">exists</span><span class="p">()</span>  <span class="c1"># 最多等待5秒，返回是否exists</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="section" id="">
<span id="id14"></span><h2>捕获异常<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h2>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">poco.exceptions</span> <span class="kn">import</span> <span class="n">PocoTargetTimeout</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;guide_panel&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s1">&#39;ImageView&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">wait_for_appearance</span><span class="p">()</span>
<span class="k">except</span> <span class="n">PocoTargetTimeout</span><span class="p">:</span>
    <span class="c1"># 面板没有弹出来，有bug</span>
    <span class="k">raise</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">poco.exceptions</span> <span class="kn">import</span> <span class="n">PocoNoSuchNodeException</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">poco</span><span class="p">(</span><span class="s1">&#39;guide_panel&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s1">&#39;ImageView&#39;</span><span class="p">)</span>
<span class="k">try</span><span class="p">:</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">img</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
        <span class="n">img</span><span class="o">.</span><span class="n">click</span><span class="p">()</span>
<span class="k">except</span> <span class="n">PocoNoSuchNodeException</span><span class="p">:</span>
    <span class="c1"># 尝试对不存在的节点进行操作，会抛出此异常</span>
    <span class="k">pass</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="">
<span id="id15"></span><h1>单元测试<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h1>
<p>poco是自动化框架，关于单元测试请见<a class="reference external" href="http://git-qa.gz.netease.com/maki/PocoUnit">PocoUnit</a>。PocoUnit提供了一整套完整的断言方法，并且和python标准库unittest是兼容的。</p>
<!-- chinese only --><div class="section" id="">
<span id="id16"></span><h2>接入参考<a class="headerlink" href="#" title="Permalink to this headline">¶</a></h2>
<ol class="simple">
<li>safaia版本需要高于1.2.0，如果不高于的话项目组master可在<a class="reference external" href="http://hunter.nie.netease.com/mywork/project#/">项目</a>页直接下载最新版的接入模块。</li>
<li>在项目的<code class="docutils literal"><span class="pre">__init__</span></code>指令后面插入以下代码片段，然后重启游戏即可，以下是NeoX引擎的例子，其余引擎的sdk正在更新中，敬请期待。</li>
</ol>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="c1"># poco uiautomation</span>
<span class="n">PocoUiautomation</span> <span class="o">=</span> <span class="n">require</span><span class="p">(</span><span class="s1">&#39;support.poco.neox.uiautomation&#39;</span><span class="p">)</span>
<span class="n">Safaia</span><span class="p">()</span><span class="o">.</span><span class="n">install</span><span class="p">(</span><span class="n">PocoUiautomation</span><span class="p">)</span>

<span class="c1"># inspector extension</span>
<span class="n">InspectorExt</span> <span class="o">=</span> <span class="n">require</span><span class="p">(</span><span class="s1">&#39;support.poco.safaia.inspector&#39;</span><span class="p">)</span>
<span class="n">InspectorExt</span><span class="o">.</span><span class="n">screen</span> <span class="o">=</span> <span class="n">require</span><span class="p">(</span><span class="s1">&#39;support.poco.neox.screen&#39;</span><span class="p">)()</span>
<span class="n">InspectorExt</span><span class="o">.</span><span class="n">dumper</span> <span class="o">=</span> <span class="n">require</span><span class="p">(</span><span class="s1">&#39;support.poco.neox.Dumper&#39;</span><span class="p">)()</span>
<span class="n">Safaia</span><span class="p">()</span><span class="o">.</span><span class="n">install</span><span class="p">(</span><span class="n">InspectorExt</span><span class="p">)</span>
</pre></div>
</div>
<ol class="simple">
<li><a class="reference external" href="http://hunter.nie.netease.com">hunter终端</a> 右上角点击<strong>Inspector</strong>按钮打开检视器面板。</li>
</ol>
<!-- end of chinese only --></div>
</div>


           </div>
           <div class="articleComments">
            
           </div>
          </div>
          <footer>
  

  <hr/>

  <div role="contentinfo">
    <p>
        &copy; Copyright 2017, NetEase Co, Ltd..

    </p>
  </div>
  Built with <a href="http://sphinx-doc.org/">Sphinx</a> using a <a href="https://github.com/snide/sphinx_rtd_theme">theme</a> provided by <a href="https://readthedocs.org">Read the Docs</a>. 

</footer>

        </div>
      </div>

    </section>

  </div>
  


  

    <script type="text/javascript">
        var DOCUMENTATION_OPTIONS = {
            URL_ROOT:'../',
            VERSION:'',
            COLLAPSE_INDEX:false,
            FILE_SUFFIX:'.html',
            HAS_SOURCE:  true,
            SOURCELINK_SUFFIX: '.txt'
        };
    </script>
      <script type="text/javascript" src="../_static/jquery.js"></script>
      <script type="text/javascript" src="../_static/underscore.js"></script>
      <script type="text/javascript" src="../_static/doctools.js"></script>

  

  
  
    <script type="text/javascript" src="../_static/js/theme.js"></script>
  

  
  
  <script type="text/javascript">
      jQuery(function () {
          SphinxRtdTheme.StickyNav.enable();
      });
  </script>
   

</body>
</html>