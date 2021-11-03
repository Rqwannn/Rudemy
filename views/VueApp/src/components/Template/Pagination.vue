<template>
    <div>
        <!-- {% if query.has_other_pages %} -->
        <div class="pagination">
            <ul class="container">
                <!-- {% if query.has_previous %} -->
                <li><a href="#" class="btn page-link" data-page="#">Prev</a></li>
                <!-- {% endif %} -->

                <!-- {% for result in custom_range %} -->
                <!-- {% if result == query.number %} -->
                    <li><a href="#" class="btn page-link btn--sub" data-page="#">#</a></li>
                    <!-- {% else %} -->
                    <li><a href="#" class="btn page-link" data-page="#">#</a></li>
                <!-- {% endif %} -->
                <!-- {% endfor %} -->

                <!-- {% if query.has_next %} -->
                <li><a href="#" class="btn page-link" data-page="#">Next</a></li>
                <!-- {% endif %} -->
            </ul>
        </div>
        <!-- {% endif %} -->
    </div>
</template>