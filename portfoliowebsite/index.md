---
layout: page
title: S Mahmudul Hasan
subtitle: Seeking full-time opportunities starting May 2024
# cover-img: /assets/img/bgm.jpg
---
<span style="font-size: 1.3rem;">Hey there! Thanks for dropping by.</span>

<span style="font-size: 1.3rem;">I am S Mahmudul Hasan, on the verge of completing my **Master's in Computer Science** at **Syracuse University**. As a software engineer and data scientist, I possess a robust skill set in software engineering, data science, and machine learning.</span>

<span style="font-size: 1.3rem;">I'm passionate about exploring cutting-edge tech, especially in software. Beyond coding, I enjoy long road trips and firmly stand by coffee in the tea vs. coffee debate.</span>


<div  id="bottomContent" class="d-flex flex-column justify-content-end align-items-center">
    <button id="profileViewButton" type="button" class="btn btn-dark d-flex align-items-center justify-content-center rounded-pill" title="Total profile visits">
        <i class="fa fa-eye mr-2"></i>
        <img id="profileViewButtonLoadingImage" width="20px" src="/assets/img/loading.gif" class="mr-2">
        <span class="badge badge-light centered-span" id="profileViewCount"></span>
        <span id="hoverText" class="position-absolute start-0 bottom-100 bg-dark text-white px-2 py-1 rounded invisible">Hover Text</span>
    </button>
</div>

<style>
  #profileViewButton:hover {
      background-color: #343a40 !important;
  }
</style>

<!-- FOLLOWING CODE GENERATES HTML LIST PAGES USING THE POSTS -->

<!-- <div class="posts-list">
  {% for post in paginator.posts %}
  <article class="post-preview">
    <a href="{{ post.url | relative_url }}">
	  <h2 class="post-title">{{ post.title }}</h2>

	  {% if post.subtitle %}
	  <h3 class="post-subtitle">
	    {{ post.subtitle }}
	  </h3>
	  {% endif %}
    </a>

    <p class="post-meta">
      Posted on {{ post.date | date: site.date_format }}
    </p>

    <div class="post-entry-container">
      {% if post.image %}
      <div class="post-image">
        <a href="{{ post.url | relative_url }}">
          <img src="{{ post.image | relative_url }}">
        </a>
      </div>
      {% endif %}
      <div class="post-entry">
        {{ post.excerpt | strip_html | xml_escape | truncatewords: site.excerpt_length }}
        {% assign excerpt_word_count = post.excerpt | number_of_words %}
        {% if post.content != post.excerpt or excerpt_word_count > site.excerpt_length %}
          <a href="{{ post.url | relative_url }}" class="post-read-more">[Read&nbsp;More]</a>
        {% endif %}
      </div>
    </div>

    {% if post.tags.size > 0 %}
    <div class="blog-tags">
      Tags:
      {% if site.link-tags %}
      {% for tag in post.tags %}
      <a href="{{ '/tags' | relative_url }}#{{- tag -}}">{{- tag -}}</a>
      {% endfor %}
      {% else %}
        {{ post.tags | join: ", " }}
      {% endif %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>

{% if paginator.total_pages > 1 %}
<ul class="pager main-pager">
  {% if paginator.previous_page %}
  <li class="previous">
    <a href="{{ paginator.previous_page_path | relative_url }}">&larr; Newer Posts</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="next">
    <a href="{{ paginator.next_page_path | relative_url }}">Older Posts &rarr;</a>
  </li>
  {% endif %}
</ul>
{% endif %} -->
