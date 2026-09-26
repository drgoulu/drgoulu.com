module github.com/HugoBlox/kit/templates/blog

go 1.21

require (
	github.com/HugoBlox/kit/modules/blox v0.0.0-20260527025321-61f41d3667f1
	github.com/HugoBlox/kit/modules/integrations/netlify v0.0.0-20260327032542-ef8ed449c7e8
)

require (
	github.com/drgoulu/backlinks4hugo v0.0.0-00010101000000-000000000000 // indirect
	github.com/drgoulu/headless-cms v0.0.0-20260922195411-0d741f896343 // indirect
	github.com/goulu/altmetric4hugo v0.0.0-20260830112131-f7ced6beec3d // indirect
	github.com/goulu/openbook4hugo v0.0.0-20260824202545-558dfae2ba58 // indirect
)

replace github.com/drgoulu/backlinks4hugo => ../backlinks4hugo
