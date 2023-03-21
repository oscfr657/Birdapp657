from django.core.exceptions import FieldError

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock


class LinkBirdBlock(blocks.StructBlock):
    font_color = blocks.CharBlock(required=False, null=True)
    bg_color = blocks.CharBlock(required=False, null=True)
    page_link = blocks.PageChooserBlock(required=False, help_text='Link to a page.')
    external_link = blocks.URLBlock(
        label='Link URL', max_length=200, required=False, help_text='Link to a URL.'
    )
    text = blocks.CharBlock(required=False, null=True, help_text='Link text')

    class Meta:
        label = 'Link'
        template = 'blocks/link.html'


class HeroBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, null=True, help_text='Block class')

    muted = blocks.BooleanBlock(required=False, default=True, help_text='Muted')
    autoplay = blocks.BooleanBlock(required=False, default=False, help_text='Autoplay')
    loop = blocks.BooleanBlock(required=False, default=False, help_text='Loop')
    controls = blocks.BooleanBlock(required=False, default=True, help_text='Controls')
    block_media = AbstractMediaChooserBlock(required=False, null=True)

    image = ImageChooserBlock(required=False, null=True)

    full_screen = blocks.BooleanBlock(
        required=False, default=False, help_text='Full screen'
    )

    font_color = blocks.CharBlock(required=False, null=True)
    bg_color = blocks.CharBlock(required=False, null=True)
    text_align = blocks.CharBlock(required=False, default='left')
    text = blocks.RichTextBlock(
        required=False,
        features=[
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'bold',
            'italic',
            'link',
            'document-link',
            'ol',
            'ul',
        ],
    )

    button_link = LinkBirdBlock(required=False, null=True)

    class Meta:
        label = 'Hero'
        icon = 'image'
        template = 'blocks/hero.html'
        group = 'Heroes'


class HeroBTBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, null=True, help_text='Block class')
    full_screen = blocks.BooleanBlock(
        required=False, default=False, help_text='Full screen'
    )

    font_color = blocks.CharBlock(required=False, null=True)
    bg_color = blocks.CharBlock(required=False, null=True)
    text_align = blocks.CharBlock(required=False, default='left')
    text = blocks.RichTextBlock(
        required=False,
        features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'document-link'],
    )

    button_link = LinkBirdBlock(required=False, null=True)

    class Meta:
        label = 'HeroBT'
        icon = 'text'
        template = 'blocks/hero_bt.html'
        group = 'Heroes'


class RacerBirdBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=False,
        features=[
            'h2',
            'h3',
            'h4',
            'h5',
            'bold',
            'italic',
            'link',
            'document-link',
            'ol',
            'ul',
        ],
    )
    image = ImageChooserBlock(required=False)
    page_image_link = blocks.PageChooserBlock(
        required=False, help_text='Link image to a page.'
    )
    external_image_link = blocks.URLBlock(
        label='Link URL',
        max_length=200,
        required=False,
        help_text='Link image to a URL.',
    )
    right = blocks.BooleanBlock(
        required=False, help_text='Image to the right else left'
    )
    bg_color = blocks.CharBlock(default='#fff', label='Background color')
    text_color = blocks.CharBlock(default='#000', label='Text color')
    block_class = blocks.CharBlock(required=False, help_text='Block class')

    class Meta:
        group = 'Racers'
        label = 'Racer'
        icon = 'image'
        template = 'blocks/racer.html'


class SimpleRacerBirdBlock(RacerBirdBlock):
    class Meta:
        group = 'Racers'
        label = 'SimpleRacerBlock'
        icon = 'image'
        template = 'blocks/simple_racer.html'


class FeedBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, help_text='Block class')
    children = blocks.ChoiceBlock(
        choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True,
    )
    parent_page = blocks.PageChooserBlock(label='parent page')
    exclude = blocks.ListBlock(
        blocks.PageChooserBlock(label="Exclude page"), required=False, default=[]
    )
    tags = blocks.ListBlock(blocks.CharBlock(label="Tag"), required=False)
    show_title = blocks.BooleanBlock(required=False, default=True)
    show_intro = blocks.BooleanBlock(required=False, default=False)
    show_content = blocks.BooleanBlock(required=False, default=False)
    show_meta = blocks.BooleanBlock(required=False, default=False)
    show_author = blocks.BooleanBlock(required=False, default=False)
    show_date = blocks.BooleanBlock(required=False, default=False)
    use_grid_template = blocks.BooleanBlock(required=False, default=False)
    bg_color = blocks.CharBlock(default='white', label='Background color')
    text_color = blocks.CharBlock(default='black', label='Text color')
    max_number = blocks.IntegerBlock(required=False)

    class Meta:
        label = 'FeedBlock'
        icon = 'list-ul'
        template = 'blocks/feed_bird_block.html'

    def get_context(self, value):
        context = super(FeedBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            feed_posts = (
                value['parent_page']
                .get_children()
                .live()
                .public()
                .filter(go_live_at__isnull=False)
                .order_by('-go_live_at')
                .distinct()
            )
        elif value['children'] == 'd':
            feed_posts = (
                value['parent_page']
                .get_descendants()
                .live()
                .public()
                .filter(go_live_at__isnull=False)
                .order_by('-go_live_at')
                .distinct()
            )
        try:
            exclude = [excl.pk for excl in value['exclude']]
            feed_posts = feed_posts.exclude(id__in=exclude)
        except AttributeError:
            pass
        tags = value['tags']
        posts = []
        for post in feed_posts.specific():
            try:
                if tags:
                    if set(post.tags.all().values_list('name', flat=True)).intersection(
                        set(tags)
                    ):
                        post = post
                    else:
                        continue
                if post.image:
                    posts.append(post)
            except (FieldError, AttributeError):
                pass
        feed_posts = posts
        max_number = value['max_number']
        if max_number:
            feed_posts = feed_posts[:max_number]
        context['feed_posts'] = feed_posts
        return context


class GridBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, help_text='Block class')
    children = blocks.ChoiceBlock(
        choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True,
    )
    parent_page = blocks.PageChooserBlock(label='parent page')
    exclude = blocks.ListBlock(
        blocks.PageChooserBlock(label="Exclude page"), required=False
    )
    tags = blocks.ListBlock(blocks.CharBlock(label="Tag"), required=False)
    show_meta = blocks.BooleanBlock(required=False, default=True)
    title_page = blocks.PageChooserBlock(required=False, label='Title page')
    bg_color = blocks.CharBlock(default='white', label='Background color')
    title_color = blocks.CharBlock(default='black', label='Title color')
    bg_text_color = blocks.CharBlock(default='white', label='Background text color')
    text_color = blocks.CharBlock(default='black', label='Text color')
    max_number = blocks.IntegerBlock(required=False)

    class Meta:
        group = 'GridBlock'
        label = 'GridBlock'
        icon = 'list-ul'
        template = 'blocks/grid_bird_block.html'

    def get_context(self, value):
        context = super(GridBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            grid_posts = (
                value['parent_page']
                .get_children()
                .live()
                .public()
                .filter(go_live_at__isnull=False)
                .order_by('-go_live_at')
                .distinct()
            )
        elif value['children'] == 'd':
            grid_posts = (
                value['parent_page']
                .get_descendants()
                .live()
                .public()
                .filter(go_live_at__isnull=False)
                .order_by('-go_live_at')
                .distinct()
            )
        try:
            exclude = [excl.pk for excl in value['exclude']]
            grid_posts = grid_posts.exclude(id__in=exclude)
        except AttributeError:
            pass
        tags = value['tags']
        posts = []
        for post in grid_posts.specific():
            try:
                if tags:
                    if set(post.tags.all().values_list('name', flat=True)).intersection(
                        set(tags)
                    ):
                        post = post
                    else:
                        continue
                if post.image:
                    posts.append(post)
            except (FieldError, AttributeError):
                pass
        grid_posts = posts
        max_number = value['max_number']
        if max_number:
            grid_posts = grid_posts[:max_number]
        context['grid_posts'] = grid_posts
        return context


class SimpleGridBirdBlock(GridBirdBlock):
    class Meta:
        group = 'GridBlock'
        label = 'SimpleGridBlock'
        icon = 'list-ul'
        template = 'blocks/simple_grid_bird_block.html'


class HighGridBirdBlock(GridBirdBlock):
    class Meta:
        group = 'GridBlock'
        label = 'HighGridBlock'
        icon = 'list-ul'
        template = 'blocks/high_grid_bird_block.html'


class BirdCodeBlock(blocks.StructBlock):  # TODO: Rename to CodeBirdBlock ?

    code = blocks.TextBlock(required=True)

    class Meta:
        label = 'Code'
        icon = 'code'
        template = 'blocks/code.html'


class HTMLBirdBlock(blocks.StructBlock):

    html = blocks.RawHTMLBlock()

    class Meta:
        label = 'HTML'
        icon = 'code'
        template = 'blocks/html_bird_block.html'


class MediaFileBirdBlock(blocks.StructBlock):
    block_width = blocks.CharBlock(required=False, help_text='Block width class')
    muted = blocks.BooleanBlock(required=False, default=True, help_text='Muted')
    autoplay = blocks.BooleanBlock(required=False, default=False, help_text='Autoplay')
    loop = blocks.BooleanBlock(required=False, default=False, help_text='Loop')
    controls = blocks.BooleanBlock(required=False, default=True, help_text='Controls')
    block_media = AbstractMediaChooserBlock()

    class Meta:
        label = 'MediaFile'
        icon = 'media'
        template = 'blocks/media_file_bird_block.html'


class ColumnBirdBlock(blocks.StreamBlock):
    bg_color = blocks.CharBlock(default='white', label='Background color')
    text_color = blocks.CharBlock(default='black', label='Text color')
    paragraph = blocks.RichTextBlock(
        required=False,
        null=True,
        features=[
            'h2',
            'h3',
            'h4',
            'bold',
            'italic',
            'superscript',
            'subscript',
            'strikethrough',
            'ol',
            'ul',
            'hr',
            'link',
            'document-link',
            'blockquote',
            'embed',
            'image',
        ],
    )
    html = HTMLBirdBlock(required=False, null=True)

    class Meta:
        template = 'blocks/columns.html'
        max_num = 7
        block_counts = {
            'bg_color': {'min_num': 1, 'max_num': 1},
            'text_color': {'min_num': 1, 'max_num': 1},
        }
