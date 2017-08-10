import argparse, os, os.path
import simpleamt
import json

if __name__ == '__main__':
  parser = argparse.ArgumentParser(parents=[simpleamt.get_parent_parser()])
  parser.add_argument('--html_template', required=True)
  parser.add_argument('--rendered_html', required=True)
  parser.add_argument('--input_json_file', type=argparse.FileType('r'))
  args = parser.parse_args()

  env = simpleamt.get_jinja_env(args.config)
  template = env.get_template(args.html_template)

  # load input from json file
  line = [item.rstrip() for item in args.input_json_file]
  hit_input = json.loads(line[0])
  
  html = template.render({'input': json.dumps(hit_input)})
  with open(args.rendered_html, 'w') as f:
    f.write(html)

